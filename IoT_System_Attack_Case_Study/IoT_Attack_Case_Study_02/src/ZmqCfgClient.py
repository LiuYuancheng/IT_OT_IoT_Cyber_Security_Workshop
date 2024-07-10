#-----------------------------------------------------------------------------
# Name:        ZmqCfgClient.py
#
# Purpose:     This module is a simple ZMQ client program to fetch the IoT config 
#              data from the IoT ZMQ server and analyze the feedback data.
#
# Version:     v_0.0.2
# Created:     2024/07/10
# Copyright:   Copyright (c) 2023 LiuYuancheng
# License:     MIT License
#-----------------------------------------------------------------------------

import zmq
import pickle

#iotIP = '172.23.155.209'
iotIP = '127.0.0.1'
port = 3003
# Init client
context = zmq.Context()
print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://%s:%s" % (iotIP, port))
# Send request
print("Sending request btyes via ZMQ client:")
configData = {
    'TEST_MD': None , 
    'RADAR_TYPE':None,
    'RADAR_PORT': None,
    'RADAR_UPDATE_INTERVAL': None,
    'RPT_MD': None,
    'RPT_INT': None,
    'RPT_SER_IP': None,
    'RPT_SER_PORT': None,
    'WEB_PORT': None
}
pickledata = pickle.dumps(configData, protocol=pickle.HIGHEST_PROTOCOL)
print(str(pickledata))
socket.send(pickledata)
# Get reply
replyData = socket.recv()
print("Received reply bytes:")
print(str(replyData))
reqDict = pickle.loads(replyData)
print ("Received reply: \n %s" %str(reqDict))
