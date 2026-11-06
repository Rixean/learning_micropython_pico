import machine # makes hardware abstraction layer available
import utime # make sleep available to control flow of code execution
import urandom # makes creation of random numbers available

led = machine.Pin(15, machine.Pin.OUT)

# initialize button pin explicitly as pull down, otherwise pin will always have high
# current/voltage
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
