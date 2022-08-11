from machine import Pin
from time import sleep

import tm1638

tm = tm1638.TM1638(stb=Pin('P8'), clk=Pin('P9'), dio=Pin('P10'))
green = Pin("P5", Pin.OUT_PP, 0)
yellow = Pin("P4", Pin.OUT_PP, 0)
red = Pin("P3", Pin.OUT_PP, 0)

green.low()
yellow.low()
red.low()

tm.clear()

def down_count(display, deley):

    while deley > 0:
        display.show(f"{deley}")
        sleep(0.5)
        deley = deley - 0.5

    display.clear()


while True:

    tm.show("3.5")

    green.high()
    sleep(1)
    tm.show("2.5")
    sleep(1)
    tm.show("1.5")

    green.low()
    sleep(0.5)
    tm.show("1")

    green.high()
    sleep(0.5)
    tm.show("0.5")

    green.low()
    sleep(0.5)
    tm.show("1")

    yellow.high()
    down_count(tm, 3.5)

    yellow.low()
    red.high()
    down_count(tm, 5)

    yellow.high()
    down_count(tm, 5)

    red.low()
    yellow.low()
    green.high()
    sleep(2)
