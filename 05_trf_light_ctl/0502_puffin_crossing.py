import machine # for assigning pins
import utime   # for timing lights
import _thread # for running second thread beside main

# define traffic light variables
led_red = machine.Pin(15, machine.Pin.OUT)
led_ylw = machine.Pin(14, machine.Pin.OUT)
led_grn = machine.Pin(13, machine.Pin.OUT)

# define variables vor crossing
btn = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
bzr = machine.Pin(12, machine.Pin.OUT)

global btn_prs # global variable will be accessed by all threads
btn_prs = False # initiate butten as not pressed

# function that runs in separate thread to read button state
# and assign global button press
def button_reader_thread():
    global btn_prs
    while True:
        if btn.value() == 1:
            print("thread 2: button pressed ")
            btn_prs = True

# launch second thread and continue main thread
_thread.start_new_thread(button_reader_thread, ())

def run_traffic_light_sequence():
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

def run_puffin_crossing_sequence():
    global btn_prs
    led_red.value(1)
    if btn_prs == True:
        for i in range(10):
            bzr.value(1)
            utime.sleep(0.2)
            bzr.value(0)
            utime.sleep(0.2)
        btn_prs = False

# continuing main thread
while True:
    run_puffin_crossing_sequence()
    run_traffic_light_sequence()

