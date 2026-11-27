##############################################################################################
# name       : Potentiometer
# version    : 0801
# description: - testing a potentiometer without voltage divider
##############################################################################################

import machine
import utime

# rotary potentiometer, wire in middle surrounded by resistor connected to 2 wires
# configure pin GP26 as 1st channel
potentiometer = machine.ADC(26)

while True:
    print(potentiometer.read_u16())
    utime.sleep(2)

# ADC -> Analog to Digital Converter: converts analog signal to digital
#       -> Resolution: measured in bits 
#           pico = 12 bits, value range 0 - 4095
#           micropython transforms range to 0 - 65,535 (16 bit) (convention)
#       -> Channels: total analog signals for conversion
#           GP26 = GP26_ADC0 = channel 0
#           GP27 = GP27_ADC1 = channel 1
#           GP28 = GP28_ADC2 = channel 2
#           4th channel connected to internal temperature sensor
