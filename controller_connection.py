# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Randall Woodall
# July 2021
# controller_connection.py
# Need a handle to each controller.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import socket


class controller_connection:
    def __init__(self, ip, port):
        self.signal = 0
        self.connection = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.connection.bind((ip, port))

     def listener(self):
        while True:
            self.signal = self.connection.recv(1024)[0]
