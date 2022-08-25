from time import sleep

from machine import Pin, SPI
from pyb import Switch

import max7219
import tm1638
from buzzer import Buzzer
from delay_service import DelayService
from traffic_light import TrafficLight


def display_show(display, str):
    display.fill(0)
    display.text(str, 0, 0, 1)
    display.show()


spi = SPI(2)
display = max7219.Matrix8x8(spi, Pin('B12'), 4)

tm = tm1638.TM1638(stb=Pin('P8'), clk=Pin('P9'), dio=Pin('P10'))



traffic_light1 = TrafficLight("P3", "P4", "P5")
traffic_light2 = TrafficLight("P0", "P1", "P2")


sw = Switch()
tm.clear()

buzzer = Buzzer(Pin("P12"), 500)

delay_service = DelayService(tm, buzzer)

while True:

    display_show(display, "STOP")

    traffic_light1.stop()
    traffic_light2.go()

    while not sw.value():
        sleep(0.1)

    delay_service.down_blink_and_count(5, traffic_light2.green)

    display_show(display, "READY")

    traffic_light1.ready()
    traffic_light2.fast()


    delay_service.down_count(3)

    traffic_light1.go()
    traffic_light2.stop()

    display_show(display, "GO")

    traffic_light1.fast()
    traffic_light2.ready()
    delay_service.down_count(3)

    display.fill(0)
    display.show()
    delay_service.down_blink_and_count(3, traffic_light1.green)

    traffic_light1.fast()
    sleep(0.5)
    tm.show("1")

    display_show(display, "FAST")

    traffic_light1.stop()
    traffic_light2.go()

    delay_service.down_count(3.5)

    traffic_light1.stop()
    traffic_light2.go()

