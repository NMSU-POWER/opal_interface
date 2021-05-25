import socket
import struct
import threading

mySocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
mySocket.bind(('169.254.8.179', 25000))
mySend = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

value = 1
inVal = 1.0

def recVal():
    global inVal
    while True:
        # mySocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # mySocket.bind(('169.254.8.179', 25000))
        pair = mySocket.recvfrom(64)
        # mySocket.close()
        inVal = struct.unpack_from('d', pair[0], 0)[0]
        print(inVal)

recThread = threading.Thread(target=recVal).start()
while True:
    unchanged = True
    if inVal >= 250:
        if value == 1:
            unchanged = False
        value = 0
    else:
        if value == 0:
            unchanged = False
        value = 1
    if not unchanged:
        mySend.sendto(struct.pack('i', value), ('169.254.157.53', 25001))
