from encodings import utf_8
from pydoc import plain
import socket
import binascii
from Crypto.Cipher import AES
import json
import crypt2

def toAscii(a):
    input_string=int(a, 2)
    Total_bytes= (input_string.bit_length() +7) // 8
    input_array = input_string.to_bytes(Total_bytes, "big")
    ASCII_value=input_array.decode()
    return bytes(ASCII_value, encoding='utf-8')

key = "DjH5H5V$u1kheUzhN@WEf3IeS9TX@aHz"
UDP_IP = ''
UDP_PORT = 28960
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(8192)
    jdat = json.loads(data)
    cpr = str(toAscii(jdat['CIPHER']))
    print(cpr)
    x = cpr.rstrip("'")
    y = x.lstrip("b'")
    plaintext = crypt2.decrypt(key, y)
    ptfn = plaintext.lstrip('"b')
    ptfn2 = ptfn.rstrip('"')
    print("received message: %s" % ptfn)