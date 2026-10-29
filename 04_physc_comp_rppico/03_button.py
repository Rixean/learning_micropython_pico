import machine
import utime

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
button.value(0)

led_ext = machine.Pin(15, machine.Pin.OUT)
count = 0

while True:
    if button.value() == 1:
        count = count + 1
        print("button pressed ", count, "times!")
        led_ext.value(1)
        #utime.sleep(1.5)
    else:
        led_ext.value(0)
