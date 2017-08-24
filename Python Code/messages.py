#!/usr/bin/env python

"""
Summary:    This file is meant to establish the message header format and can be called to create a message header

Created:    July 27th, 2017
Author:     Ryan Decker

Change Log:

"""


import time

def addHeader(message_type):
    header = []
    syncMsg = ["DE", "AD", "BE", "EF"]

    message_type = hex(int(message_type))[2:4]      # Extract the message type from the function pass
    if len(message_type) < 2:
        message_type = "0" + message_type
    for word in syncMsg:
        header.append(word)
    header.append(message_type)
    for time_word in time.gmtime():
        time_word = hex(time_word)[2:4]
        header.append(time_word)
    while len(header) < 16:
        header.append("00")
    for index in range(0, len(header)):
        if len(header[index]) < 2:
            header[index] = "0" + header[index]
    header_string = ' '.join(header)
    header_string += " "
    return header_string

def addBuffer(message):
    message_array = message.split(' ')
    while len(message_array) < 60:
        message_array.append("00")
    message = " ".join(message_array)
    return message
