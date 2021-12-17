import socket   
import sys  
import struct
import time
import numpy as np
import time

TCP_IP = '127.0.0.1'  # set these to the COSMOS instance
TCP_PORT = 8080 # set these to the COSMOS instance

IDENTIFIER_WORD = 0xfe6b
BYTE_ORDER = 'big'
word_size = np.uint8

# create a telemetry packet that is consistent with the definition for COSMOS (tlm.txt)
class tlm_packet(object):
    """A basic telemetry packet."""
    def __init__(self, identifier:np.uint16, value:np.uint32, flag:bool):
        self.data = np.zeros(7, dtype=word_size)
        print(IDENTIFIER_WORD.to_bytes(2, byteorder=BYTE_ORDER))
        self.data[0:2] = np.frombuffer(IDENTIFIER_WORD.to_bytes(2, byteorder=BYTE_ORDER), dtype=word_size)
        self.data[2:6] = np.frombuffer(value.to_bytes(4, byteorder=BYTE_ORDER), dtype=word_size)
        self.data[6] = flag

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

packet = tlm_packet(IDENTIFIER_WORD, 34530, True)

packet_value = 0
packet_flag = True

while(True):
    packet = tlm_packet(IDENTIFIER_WORD, packet_value, packet_flag)
    s.send(packet)
    packet_flag = not packet_flag
    packet_value += 1
    time.sleep(1)


#data = s.recv(BUFFER_SIZE)
#s.close()
#print("received data:", data)