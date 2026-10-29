from machine import Pin
import utime

button = Pin(14, Pin.IN)
count = 0

while True:
    if button.value() == 1:
        count = count + 1
        print("button pressed ", count, "times!")
        utime.sleep(1.5)
