from pipe import Pipe
from time import sleep


## GLOBALS ##
PIPENAME = "monitorpipe"

if __name__ == "__main__":
    pipein = Pipe(PIPENAME, "READ")

    while True:
        print "READER:", pipein.Read()
        sleep(30)
