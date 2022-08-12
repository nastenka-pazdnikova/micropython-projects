from machine import Pin
from time import sleep

from pyb import Switch

import tm1638

tm = tm1638.TM1638(stb=Pin('P8'), clk=Pin('P9'), dio=Pin('P10'))
green = Pin("P5", Pin.OUT_PP, 0)
yellow = Pin("P4", Pin.OUT_PP, 0)
red = Pin("P3", Pin.OUT_PP, 0)

green.low()
yellow.low()
red.low()

sw = Switch()
tm.clear()

def down_count(display, deley):

    while deley > 0:
        display.show(f"{deley}")
        sleep(0.5)
        deley = deley - 0.5

    display.clear()


def down_blink_and_count(display, deley, led):

    while deley > 0:
        if led.value():
            led.low()
        else:
            led.high()
        display.show(f"{deley}")
        sleep(0.5)
        deley = deley - 0.5

    display.clear()


while True:

    red.high()

    while not sw.value():
        sleep(0.1)

    down_count(tm, 3)

    yellow.high()
    down_count(tm, 3)

    red.low()
    yellow.low()
    green.high()
    down_count(tm, 3)
    down_blink_and_count(tm, 3, green)

    green.low()
    sleep(0.5)
    tm.show("1")

    yellow.high()
    down_count(tm, 3.5)

    yellow.low()
    red.high()

