from encodings import utf_8
import send
import socket
import json
import crypt2
import asyncio
from threading import Thread
key = "DjH5H5V$u1kheUzhN@WEf3IeS9TX@aHz"
UDP_IP = ''
UDP_PORT = 28960
def toAscii(a):
    input_string=int(a, 2)
    Total_bytes= (input_string.bit_length() +7) // 8
    input_array = input_string.to_bytes(Total_bytes, "big")
    ASCII_value=input_array.decode()
    return bytes(ASCII_value, encoding='utf-8')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
def listen():
    while True:
        data, addr = sock.recvfrom(8192)
        jdat = json.loads(data)
        cpr = str(toAscii(jdat['CIPHER']))
        x = cpr.rstrip("'")
        y = x.lstrip("b'")
        plaintext = crypt2.decrypt(key, y)
        ptfn = plaintext.lstrip('"b')
        ptfn2 = ptfn.rstrip('"')
        print(ptfn.rstrip('"'))
def client():
    send.sendUDP(input(": "))
    asyncio.run(client())
if __name__ == '__main__':
    Thread(target = listen).start()
    Thread(target = client).start()
