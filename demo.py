import pyfirmata
import time
pin=13
port="COM9"
board=pyfirmata.Arduino(port)
while True:
    board.digital[pin].write(1)
    time.sleep(5)
    print("on")
    board.digital[pin].write(0)
    time.sleep(5)
    print("off")
