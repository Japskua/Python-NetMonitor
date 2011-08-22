#!/usr/bin/python2.5 

"""
@author: Janne Parkkila
@summary: Internet connection monitor, that watches for changes in the used 
          networking interface. Writes the result to a pipe, that can be read
          and used by other programs.

@note: Code is based to the python examples of conic by Lauro Moura <lauro.neto@indt.org.br>, 2007
"""

import conic
import dbus
import gobject
import dbus.glib
import threading
import sys
from time import time, sleep
from pipe import Pipe

## GLOBALS ##

PIPENAME = "monitorpipe"


def start():
    print "start():"
    connection = conic.Connection()
    connection.connect("connection-event", connection_cb)
    connection.connect("statistics", statistics_cb)
    connection.set_property("automatic-connection-events", True)
    
    return connection

    
def stop(connection, loop):
    print "start():"
    connection.set_property("automatic-connection-events", False)
    loop.quit()

def statistics_cb(connection, event):
    #print "statistics_cb(%s, %s)" % (connection, event)

    stats = "time active=",  event.get_time_active().__str__()
    stats += "signal strength=", event.get_signal_strength()
    stats += "rx_packets=", event.get_rx_packets()
    stats += "tx_packets=", event.get_tx_packets()
    stats += "rx_bytes=", event.get_rx_bytes()
    stats += "tx_bytes=", event.get_tx_bytes()
    
    return stats

def connection_cb(connection, event):
    #print "connection_cb(%s, %s)" % (connection, event)
    
    status = event.get_status()
    error = event.get_error()
    iap_id = event.get_iap_id()
    bearer = event.get_bearer_type()
    
    if status == conic.STATUS_CONNECTED:
        data = "CONNECTED: (%s, %s, %i, %i)" % (iap_id, bearer, status, error)
        # connection.statistics(iap_id)
        pipeout.Write(data)
    elif status == conic.STATUS_DISCONNECTED:
        data = "DISCONNECTED (%s, %s, %i, %i)" % (iap_id, bearer, status, error)
        pipeout.Write(data)
    elif status == conic.STATUS_DISCONNECTING:
        data = "DISCONNECTING (%s, %s, %i, %i)" % (iap_id, bearer, status, error)
        pipeout.Write(data)

if __name__ == "__main__":

    loop = gobject.MainLoop()
    gobject.threads_init()
    bus = dbus.SystemBus(private=True)

    print "Creating a write pipe"
    pipeout = Pipe(PIPENAME, "WRITE")

    while True:
        connection = start()
        loop.run()
        stop(connection, loop)
    
