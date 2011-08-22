#!/usr/bin/python

"""
@author: Janne Parkkila
@summary: The read-in part of the monitor. This one monitors the 
          pipe that the monitor writes to. Checks for monitor status
          updates depending on the given update timeframe.
"""

from pipe import Pipe
from time import sleep
import sys

## GLOBALS ##
PIPENAME = "monitorpipe"

if __name__ == "__main__":
    # Read the commandline arguments
    update = 30
    if "-u" in sys.argv:
        update = int(sys.argv[sys.argv.index("-u") + 1])

    pipein = Pipe(PIPENAME, "READ")

    while True:
        print "READER:", pipein.Read()
        sleep(update)
