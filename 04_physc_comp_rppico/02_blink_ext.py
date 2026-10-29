from machine import Pin
import time

led_ext = Pin(15, Pin.OUT) # external led connected to pin 20 (GP15)
led = Pin(25, Pin.OUT) # onboard led | For Pico W use: Pin("LED", Pin.OUT)

while True:
    led_ext.value(1)
    led.value(0)
    time.sleep(0.4)
    led_ext.value(0)
    led.value(1)
    time.sleep(0.4)
