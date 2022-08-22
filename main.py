from time import sleep

from pyb import Switch

import tm1638


import max7219
from machine import Pin, SPI
from pyb import Timer

spi = SPI(2)
display = max7219.Matrix8x8(spi, Pin('B12'), 4)



tm = tm1638.TM1638(stb=Pin('P8'), clk=Pin('P9'), dio=Pin('P10'))
green = Pin("P5", Pin.OUT_PP, 0)
yellow = Pin("P4", Pin.OUT_PP, 0)
red = Pin("P3", Pin.OUT_PP, 0)


green2 = Pin("P2", Pin.OUT_PP, 0)
yellow2 = Pin("P1", Pin.OUT_PP, 0)
red2 = Pin("P0", Pin.OUT_PP, 0)


def beep_on():

    tim = Timer(1, freq=500)
    ch = tim.channel(1, Timer.PWM, pin=Pin("P12"))
    ch.pulse_width_percent(50)


def beep_off():

    tim = Timer(1, freq=500)
    tim.deinit()



green.low()
yellow.low()
red.low()


green2.low()
yellow2.low()
red2.low()



sw = Switch()
tm.clear()

def down_count(display, deley):

    while deley > 0:
        display.show(f"{deley}")
        sleep(0.5)
        deley = deley - 0.5

    display.clear()


def display_show(display, str):

    display.fill(0)
    display.text(str, 0, 0, 1)
    display.show()


def down_blink_and_count(display, deley, led):

    while deley > 0:
        if led.value():
            led.low()
        else:
            led.high()
        display.show(f"{deley}")
        beep_on()
        sleep(0.25)
        beep_off()
        sleep(0.25)
        deley = deley - 0.5

    display.clear()


while True:

    display_show(display, "STOP")


    red.high()
    green2.high()


    while not sw.value():
        sleep(0.1)

    down_blink_and_count(tm, 5, green2)


    display_show(display, "WAIT")

    yellow.high()
    yellow2.high()
    green2.low()

    down_count(tm, 3)

    red.low()
    yellow.low()
    yellow2.low()

    display_show(display, "GO")

    green.high()
    red2.high()
    down_count(tm, 3)


    display.fill(0)
    display.text('RUN', 0, 0, 1)
    display.show()
    down_blink_and_count(tm, 3, green)

    green.low()
    sleep(0.5)
    tm.show("1")


    display_show(display, "FAST")

    yellow.high()
    yellow2.high()

    down_count(tm, 3.5)

    yellow.low()
    yellow2.low()
    red2.low()
    red.high()
    green2.high()
