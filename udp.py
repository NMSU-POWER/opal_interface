# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Randall Woodall
# May 2021
# udp.py
# Accept UDP data on port 25000, send UDP data back out on 25001 @ remote simulink.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import socket
import struct
import array
import threading
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as ani

mySocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
mySocket.bind(('128.123.131.66', 25000))
# mySocket.bind(('169.254.8.179', 25000))
mySend = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

value = 1
inVal = 1.0
data_record = []
fig = plt.figure()


def graph(new_value):
    global data_record
    global fig
    data_record.append(data_record)
    fig.clear()
    p = plt.plot(data_record)


def recval():
    global inVal
    global fig
    animator = ani.FuncAnimation(fig, graph, interval=100)
    # plt.show()
    while True:
        pair = mySocket.recvfrom(64)
        inVal = struct.unpack_from('d', pair[0], 0)[0]
        # print(inVal)


if __name__ == '__main__':
    # recThread = threading.Thread(target=recval).start()
    remote_ip = sys.argv[1]
    i = 0
    while True:
        i+=1
        pair, addr = mySocket.recvfrom(1024)
        inVal = array.array('d', pair)
        print(inVal)
        mySend.sendto(bytes(array.array('d', [0, 1, 2, i])), (remote_ip, 25001))
        '''unchanged = True
        if inVal >= 250:
            if value == 1:
                unchanged = False
            value = 0
        else:
            if value == 0:
                unchanged = False
            value = 1
        if not unchanged:
            mySend.sendto(struct.pack('i', value), (remote_ip, 25001))'''
