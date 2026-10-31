import machine
import utime

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
button.value(0)

led_ext = machine.Pin(15, machine.Pin.OUT)
count = 0

sleep_time = 0.3

def blinker(blinks):
    print("blinking led ", blinks, "time(s)!")
    utime.sleep(sleep_time)
    for i in range(0, blinks):
        led_ext.value(1)
        utime.sleep(sleep_time)
        led_ext.value(0)
        utime.sleep(sleep_time)

while True:
    if button.value() == 1:
        blinker(3 + 1)

#while True:
#    if button.value() == 1:
#        count = count + 1
#        print("button pressed ", count, "times!")
#        led_ext.value(1)
#        #utime.sleep(1.5)
#    else:
#        led_ext.value(0)
