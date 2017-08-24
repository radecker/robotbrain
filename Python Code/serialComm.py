#!/usr/bin/env python

"""
Summary:    This file will initiate, transmit, and receive serial communications between the raspberry pi and the
            arduino.

Created:    July 27th, 2017
Author:     Ryan Decker

Change Log:

"""

import messages
import time
import serial

def serialInit(port, baud_rate):
    ser = serial.Serial(port, baud_rate)
    return ser

def sendMsg(message, message_type):
    header = messages.addHeader(message_type)
    message = header + message + messages.addBuffer(message)
    message = message.split(' ')
    print(message)
    #bytes_written = ser.write(message)
    #return bytes_written

def readMsg(num_messages):
    message = []
    while len(message) < num_messages:
        num_bytes = 0
        while not num_bytes:
            num_bytes = ser.inWaiting()
            if num_bytes:
                time.sleep(.1)
                num_bytes = ser.inWaiting()
        message.append(ser.read(num_bytes))
    return message

def serialClose():
    ser.close()


ser = serialInit("/dev/ttyACM0", 9600)
sendMsg("FF FF FF", 3)
print(readMsg(4))

serialClose()
