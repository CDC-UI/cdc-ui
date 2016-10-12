#!/usr/bin/python
# -*- coding: utf-8 -*-
# Code is largely based on examples from Violent Python by TJ O'Connor

import re
import os
import sqlite3


def printDownloads(downloadDB):
    conn = sqlite3.connect(downloadDB)
    c = conn.cursor()
    c.execute('SELECT name, source, datetime(endTime/1000000,\
    \'unixepoch\') FROM moz_downloads;')
    print '\n[*] --- Files Downloaded --- '
    for row in c:
        print '[+] File: ' + str(row[0]) + ' from source: ' \
            + str(row[1]) + ' at: ' + str(row[2])


def printCookies(cookiesDB):
    conn = sqlite3.connect(cookiesDB)
    c = conn.cursor()
    c.execute('SELECT host, name, value FROM moz_cookies')

    print '\n[*] -- Found Cookies --'
    for row in c:
        host = str(row[0])
        name = str(row[1])
        value = str(row[2])
        print '[+] Host: ' + host + ', Cookie: ' + name \
            + ', Value: ' + value


def printHistory(placesDB):
    conn = sqlite3.connect(placesDB)
    c = conn.cursor()
    c.execute("select url, datetime(visit_date/1000000, \
      'unixepoch') from moz_places, moz_historyvisits \
      where visit_count > 0 and moz_places.id==\
      moz_historyvisits.place_id;")

    print '\n[*] -- Found History --'
    for row in c:
        url = str(row[0])
        date = str(row[1])
        print '[+] ' + date + ' - Visited: ' + url


def printGoogle(placesDB):
    conn = sqlite3.connect(placesDB)
    c = conn.cursor()
    c.execute("select url, datetime(visit_date/1000000, \
      'unixepoch') from moz_places, moz_historyvisits \
      where visit_count > 0 and moz_places.id==\
      moz_historyvisits.place_id;")

    print '\n[*] -- Found Google --'
    for row in c:
        url = str(row[0])
        date = str(row[1])
        if 'google' in url.lower():
            r = re.findall(r'q=.*\&', url)
            if r:
                search = r[0].split('&')[0]
                search = search.replace('q=', '').replace('+', ' ')
                print '[+] '+date+' - Searched For: ' + search


def main():
    pathName = 'firefox_profile\\'

    downloadDB = os.path.join(pathName, 'downloads.sqlite')
    if os.path.isfile(downloadDB):
        printDownloads(downloadDB)

    cookiesDB = os.path.join(pathName, 'cookies.sqlite')
    if os.path.isfile(cookiesDB):
        printCookies(cookiesDB)

    placesDB = os.path.join(pathName, 'places.sqlite')
    if os.path.isfile(placesDB):
        printHistory(placesDB)
        printGoogle(placesDB)

if __name__ == '__main__':
    main()
