import machine # makes hardware abstraction layer available
import utime # make sleep available to control flow of code execution
import urandom # makes creation of random numbers available

# led to visually react to
led = machine.Pin(15, machine.Pin.OUT)

# initialize button pin explicitly as pull down, otherwise pin will always have high
# current/voltage
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# callback function (handler) to run when interrupt is triggered
# interupt request (irq) allows action when button is pushed
def btn_handler(pin):
    btn.irq(handler=None) # turn handler off
    print(pin)            # print interupt pin status
    print("button interupt handler finished")

# sequence for led to turn on and off at random times
led.value(1)
utime.sleep(urandom.uniform(5, 10)) # random time between 5 and 10 seconds with uniform 
                                    # distribution
led.value(0) # switch led off to signal user to push button

# initialize interrupt request trigger
print(btn.value())
print(machine.Pin.IRQ_RISING)
btn.irq(trigger=machine.Pin.IRQ_RISING, handler=btn_handler)
# using mpremote run will not print button handler content because of the end of the script
# already reached. The usb connection is closed at that point
# by using mpremote repl, the connection stays open and the handler content will be seen in 
# the terminal
