##############################################################################################
# name       : Burglar Alarm
# version    : 0702
# description: - outputs if PIR is being triggered
#              - adds blinking led when infrared motion sensor activated
##############################################################################################

import machine # make pi pico abstraction layer available
import utime

# initialize pir like button for input
# 3.3v (high) will be sent to pin when triggered
pir_sensor = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)

# initialize global variable that indicates if motion was detected
motion_detected = False

# handler will be called using interrupt so minimal changes in preallocated memory
def pir_handler(pin):
    global motion_detected
    motion_detected = True

# arm interupt to change motion detected variable
pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

def announce_motion_detection():
    print("ALARM! Motion detected!")


while True:
    if motion_detected:
        announce_motion_detection()
        motion_detected = False

    utime.sleep_ms(50)

# print("ALARM! Motion detected!")


##############################################################################################
# HC-SR501 PIR sensor (passive infrared sensor )
# integrated in own circuit board containing the sensor, resistors, potentiometers
# potentiometers for sensitivity and activity period
##############################################################################################
