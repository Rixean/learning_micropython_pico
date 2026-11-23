##############################################################################################
# name       : Burglar Alarm
# version    : 0704
# description: - outputs if PIR is being triggered
#              - adds blinking led when infrared motion sensor activated
#              - add buzzer
#              - add second PIR
##############################################################################################

import machine # make pi pico abstraction layer available
import utime

# initialize pir like button for input
# 3.3v (high) will be sent to pin when triggered
pir_01 = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
pir_02 = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_DOWN)

# initialize buzzer
buzr = machine.Pin(14, machine.Pin.OUT)

# initialize led pin and let it light for 1 second to state program start
led = machine.Pin(15, machine.Pin.OUT)
led.value(1)
utime.sleep(1)
led.value(0)

# initialize global variable that indicates if motion was detected
motion_detected = False
led_blinking = False
pir_nr = 0

# handler will be called using interrupt so minimal changes in preallocated memory
def pir_handler(pin):
    global motion_detected
    motion_detected = True

    # assign number of activated pir based on pin number
    global pir_nr
    if pin is pir_01:
        pir_nr = 1
    elif pin is pir_02:
        pir_nr = 2

# set interupt to pause main execution and change motion detected variable
pir_01.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)
pir_02.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

def announce_motion_detection(nr):
    print("ALARM! Motion detected! at sensor " + str(nr) + ".")

    # blink led and set status
    global led_blinking
    led_blinking = True
    for i in range(30):
        led.toggle()
        buzr.toggle()
        utime.sleep_ms(100)
    led_blinking = False

    global motion_detected
    motion_detected = False

# infinite loop that keeps the program running
while True:
    if motion_detected:
        if not led_blinking:
            print("LED is off -> announce motion")
            announce_motion_detection(pir_nr)
        else:
            print("LED is On -> no announcement.")

    utime.sleep_ms(50)

# print("ALARM! Motion detected!")


##############################################################################################
# HC-SR501 PIR sensor (passive infrared sensor )
# integrated in own circuit board containing the sensor, resistors, potentiometers
# potentiometers for sensitivity and activity period

# second thread would be used if code needs to keep running continously without pause
##############################################################################################
