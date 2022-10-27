import send
import crypt2
def loop():
    send.sendUDP(input(": "))
    loop()
loop()

