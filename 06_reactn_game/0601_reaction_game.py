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

led.value(1)
utime.sleep(urandom.uniform(5, 10))
led.value(0)

btn.irq(trigger=machine.Pin.IRQ_RISING, handler=btn_handler)
