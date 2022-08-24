from time import sleep

from machine import Pin, SPI
from pyb import Switch

import max7219
import tm1638
from buzzer import Buzzer
from delay_service import DelayService


def display_show(display, str):
    display.fill(0)
    display.text(str, 0, 0, 1)
    display.show()


spi = SPI(2)
display = max7219.Matrix8x8(spi, Pin('B12'), 4)

tm = tm1638.TM1638(stb=Pin('P8'), clk=Pin('P9'), dio=Pin('P10'))
green = Pin("P5", Pin.OUT_PP, 0)
yellow = Pin("P4", Pin.OUT_PP, 0)
red = Pin("P3", Pin.OUT_PP, 0)

green2 = Pin("P2", Pin.OUT_PP, 0)
yellow2 = Pin("P1", Pin.OUT_PP, 0)
red2 = Pin("P0", Pin.OUT_PP, 0)

green.low()
yellow.low()
red.low()

green2.low()
yellow2.low()
red2.low()

sw = Switch()
tm.clear()

buzzer = Buzzer(Pin("P12"), 500)

delay_service = DelayService(tm, buzzer)

while True:

    display_show(display, "STOP")

    red.high()
    green2.high()

    while not sw.value():
        sleep(0.1)

    delay_service.down_blink_and_count(5, green2)

    display_show(display, "WAIT")

    yellow.high()
    yellow2.high()
    green2.low()

    delay_service.down_count(3)

    red.low()
    yellow.low()
    yellow2.low()

    display_show(display, "GO")

    green.high()
    red2.high()
    delay_service.down_count(3)

    display.fill(0)
    display.text('RUN', 0, 0, 1)
    display.show()
    delay_service.down_blink_and_count(3, green)

    green.low()
    sleep(0.5)
    tm.show("1")

    display_show(display, "FAST")

    yellow.high()
    yellow2.high()

    delay_service.down_count(3.5)

    yellow.low()
    yellow2.low()
    red2.low()
    red.high()
    green2.high()
