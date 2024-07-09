from struct import pack

class Serial(object):

    def __init__(self, port, bandwidth, bitNumber, parity, stopBit, timeout=1) -> None:
        pass

    def read(self, data):
        dataByte = b''
        for _ in range(2):
            data = self.dataHeader + pack('i', int(0)) + pack('i', 34)
            for _ in range(35):
                data += pack('f', round(0), 2)
            dataByte += data
        #print('read: %s' %str(dataByte))
        return dataByte
    
    def close():
        pass