from machine import Pin
import utime
#led display when person detected
led = Pin(1, Pin.OUT)
#sensor
pir = Pin(0, Pin.IN, Pin.PULL_DOWN)
#transistor responsible for tunrning on PI
pi = Pin(28, Pin.OUT)

led.value(0)

print("Starting")
utime.sleep(3)
print("Ready!")

while True:
    if (pir.value() == 1):
        print("Person Detected")
        #when person is detected turn on pi by allowing current to flow through the transistor shorting pins 5,6 of the pi
        led.value(1)
        pi.value(1)
        utime.sleep(0.2)
        return
    elif (pir.value() == 0):
        print("no one there...")
        led.value(0)
        utime.sleep(0.2)