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

# initialize led pin and let it light for 1 second to state program start
led = machine.Pin(15, machine.Pin.OUT)
led.value(1)
utime.sleep(1)
led.value(0)

# initialize global variable that indicates if motion was detected
motion_detected = False
led_blinking = False

# handler will be called using interrupt so minimal changes in preallocated memory
def pir_handler(pin):
    global motion_detected
    motion_detected = True

# arm interupt to change motion detected variable
pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

def announce_motion_detection():
    print("ALARM! Motion detected!")

    # blink led and set status
    global led_blinking
    led_blinking = True
    for i in range(30):
        led.toggle()
        utime.sleep_ms(100)
    led_blinking = False

    global motion_detected
    motion_detected = False

# infinite loop that keeps the program running
while True:
    if motion_detected:
        if not led_blinking:
            print("LED is off -> announce motion")
            announce_motion_detection()
        else:
            print("LED is On -> no announcement.")

    utime.sleep_ms(50)

# print("ALARM! Motion detected!")


##############################################################################################
# HC-SR501 PIR sensor (passive infrared sensor )
# integrated in own circuit board containing the sensor, resistors, potentiometers
# potentiometers for sensitivity and activity period
##############################################################################################
