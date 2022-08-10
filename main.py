from machine import Pin
from time import sleep

green = Pin("P5", Pin.OUT_PP, 0)
yellow = Pin("P4", Pin.OUT_PP, 0)
red = Pin("P3", Pin.OUT_PP, 0)

green.low()
yellow.low()
red.low()

while True:

    green.high()
    sleep(2)
    green.low()
    sleep(0.5)
    green.high()
    sleep(0.5)
    green.low()
    sleep(0.5)

    yellow.high()
    sleep(3.5)
    yellow.low()

    red.high()
    sleep(5)
    yellow.high()
    sleep(5)

    red.low()
    yellow.low()

    green.high()
    sleep(2)
