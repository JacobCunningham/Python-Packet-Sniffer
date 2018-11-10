from socket import *
import struct
import binascii
from packet import packet

sock = socket(AF_PACKET, SOCK_RAW, ntohs(0x003))



while True:
    data = sock.recvfrom(65535)

    packy = packet(data)

    print(packy)