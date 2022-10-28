from encodings import utf_8
import socket
from pyrsistent import b
from Crypto.Cipher import AES
import json
import crypt2

def toBytes(a):
  l, m = [], []
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(format(i, '#010b')[2:])
  return m

def sendUDP(a):
    MESSAGE = bytes(a, encoding='utf-8')
    key = "DjH5H5V$u1kheUzhN@WEf3IeS9TX@aHz"
    ciphertext = crypt2.encrypt(key, str(MESSAGE))
    UDP_IP = "255.255.255.255"
    UDP_PORT = 28960
    FXMESSAGE = ''.join(toBytes(str(ciphertext)))
    MSGJSON = {'CIPHER': str(FXMESSAGE)}
    FNMESSAGE = json.dumps(MSGJSON).encode('utf-8')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(FNMESSAGE, (UDP_IP, UDP_PORT))