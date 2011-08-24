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


class PipeReader(object):
    """
    The PipeReader class
    """
    _pipeName = None
    _pipe = None
    
    def __init__(self, pipeName):
        """
        The Class Constructor
        """
        try:
            self._pipeName = pipeName
            self._pipe = Pipe(self._pipeName, "READ")
        except Exception, instance:
            print "Exception at creating the pipereader: %s" % instance

    def Read():
        """
        @summary: This function reads the in-pipe
                  for the latest information
        @return: Returns the data from the pipe
        """
        return self._pipe.Read()
        

## GLOBALS ##
PIPENAME = "monitorpipe"

if __name__ == "__main__":
    # Read the commandline arguments
    update = 30
    if "-u" in sys.argv:
        update = int(sys.argv[sys.argv.index("-u") + 1])

   # pipein = Pipe(PIPENAME, "READ")
    pipein = PipeReader(PIPENAME)

    while True:
        print "READER:", pipein.Read()
        sleep(update)
