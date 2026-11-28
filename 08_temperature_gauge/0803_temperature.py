##############################################################################################
# name       : Potentiometer
# version    : 0802
# description: - testing a potentiometer without voltage divider
#               - introduce potentiometer as voltage divider
##############################################################################################

import machine
import utime

# rotary potentiometer, wire in middle surrounded by resistor connected to 2 wires
# configure pin GP26 as 1st channel
potentiometer = machine.ADC(26)
# voltage divider: 1 resistor pin to 3.3V and other to GND to get voltage range 0 - 3.3

conversion_factor = 3.3 / (65535)
voltage = 0.0

while True:
    voltage = potentiometer.read_u16() * conversion_factor
    # print(potentiometer.read_u16())
    print(voltage)
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
