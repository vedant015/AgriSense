import pyfirmata
import time

port="COM9"
board=pyfirmata.Arduino(port)
soil=board.get_pin('a:0:i')
pump=board.get_pin('d:7:o')
moisture_treshold=500;

it=pyfirmata.util.Iterator(board)
it.start()

# Wait for the iterator to start
time.sleep(1)

def pump_on():
    pump.write(1)

def pump_off():
    pump.write(0)
while True:
    ar=soil.read()
    x=(1-ar)*1000
    print(x)
    if x<moisture_treshold:
        pump_on()
    else:
        pump_off()
    time.sleep(10)

