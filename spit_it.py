# Music Hackathon 6/28/14
# Etsy Labs, Brooklyn NY
# Modified by Lisa Luo
# Based on "Say.py" by Jamis Johnson
#   https://github.com/jamiis/say/blob/master/say.py

import os
import string
import sys

# Format of directory name is 
dirname = str(sys.argv[1]) + "/"
files = os.listdir(dirname)
keys = list(string.ascii_lowercase)
mappings = {}

i = 0
j = 1
while j < len(files):
    mappings[keys[i]] = dirname + files[j]
    i+=1
    j+=1
print "Start rappin' doeeee"

# http://stackoverflow.com/a/4256153/939971
def spit_it(st):
    bashCommand = 'afplay ' + mappings[st]
    import subprocess
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)

# http://stackoverflow.com/a/13207724/939971
import termios, fcntl, sys, os
fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

try:
    while 1:
        try:
            c = sys.stdin.read(1)
            spit_it(c)
        except IOError: pass
finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)