##############################################################################################
# name       : Reaction Game
# version    : 0603
# description: add code to keep tty connection open and only change a global variable
#              inside interupt function to prevent memory corruption when script 
#              continues after interupt exits to script interrupt point
##############################################################################################

import machine # makes hardware abstraction layer available
import utime # make sleep available to control flow of code execution
import urandom # makes creation of random numbers available

game_over = False # global flag to track game state

# led to visually react to
led = machine.Pin(15, machine.Pin.OUT)

# initialize button pin explicitly as pull down, otherwise pin will always have high
# current/voltage
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# callback function (handler) to run when interrupt is triggered
# interupt request (irq) allows action when button is pushed
def btn_handler(pin):
    btn.irq(handler=None) # disable interrupt so it only triggers once
    # timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
    # print("Your reaction time was " + str(timer_reaction) + " milliseconds!")

    # using global variable with preallocated memory to avoid memory corruption
    global game_over # bring global variable into function
    game_over = True # set variable to exit loop after interrupt function exits

# sequence for led to turn on and off at random times
led.value(1)
utime.sleep(urandom.uniform(3, 6)) # random time between 5 and 10 seconds with uniform 
                                    # distribution
led.value(0) # switch led off to signal user to push button

timer_start = utime.ticks_ms()

# initialize interrupt request trigger
btn.irq(trigger=machine.Pin.IRQ_RISING, handler=btn_handler) #IRQ_RISING 0v -> 3.3v
# using mpremote run will not print button handler content because of the end of the script
# already reached. The usb connection is closed at that point
# by using mpremote repl, the connection stays open and the handler content will be seen in 
# the terminal

# keep script and serial listener alive until button is pressed
while not game_over:
    utime.sleep_ms(50)

timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
print("Your reaction time was " + str(timer_reaction) + " milliseconds!")
