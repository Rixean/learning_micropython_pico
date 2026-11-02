import machine
import utime

led_red = machine.Pin(15, machine.Pin.OUT)
led_ylw = machine.Pin(14, machine.Pin.OUT)
led_grn = machine.Pin(13, machine.Pin.OUT)

while True:
    led_red.value(1)
    utime.sleep(5)

    led_ylw.value(1)
    utime.sleep(2)

    led_red.value(0)
    led_ylw.value(0)
    led_grn.value(1)
    utime.sleep(5)

    led_grn.value(0)
    led_ylw.value(1)
    utime.sleep(5)

    led_ylw.value(0)
