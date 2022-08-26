from machine import Timer
from pyb import Pin


def create_traffic_light_pin(pin_name):
    return Pin(pin_name, Pin.OUT_PP, 0)

class TrafficLight:
    def __init__(self, red, yellow, green, buzzer):
        self.red = create_traffic_light_pin(red)
        self.yellow = create_traffic_light_pin(yellow)
        self.green = create_traffic_light_pin(green)
        self.buzzer = buzzer

        self.green.low()
        self.yellow.low()
        self.red.low()

        self.timer = Timer(period=500, mode=Timer.ONE_SHOT)

    def ready(self):
        self.blink_off()
        self.red.high()
        self.yellow.high()
        self.green.low()

    def stop(self):
        self.blink_off()
        self.red.high()
        self.yellow.low()
        self.green.low()


    def go(self):
        self.blink_off()
        self.red.low()
        self.yellow.low()
        self.green.high()

    def blink_green(self, param):
        if self.green.value():
            self.buzzer.beep_on()
        else:
            self.buzzer.beep_off()

        self.green.value(not self.green.value())

    def run(self):
        self.red.low()
        self.yellow.low()
        self.blink_on()
    def blink_on(self):
        self.timer.init(period=500, mode=Timer.PERIODIC, callback=self.blink_green)

    def blink_off(self):
        self.timer.deinit()
        self.buzzer.beep_off()

    def fast(self):
        self.blink_off()
        self.red.low()
        self.yellow.high()
        self.green.low()




