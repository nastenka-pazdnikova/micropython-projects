from pyb import Pin


def create_traffic_light_pin(pin_name):
    return Pin(pin_name, Pin.OUT_PP, 0)

class TrafficLight:
    def __init__(self, red, yellow, green):
        self.red = create_traffic_light_pin(red)
        self.yellow = create_traffic_light_pin(yellow)
        self.green = create_traffic_light_pin(green)

        self.green.low()
        self.yellow.low()
        self.red.low()

    def ready(self):
        self.red.high()
        self.yellow.high()
        self.green.low()

    def stop(self):
        self.red.high()
        self.yellow.low()
        self.green.low()


    def go(self):
        self.red.low()
        self.yellow.low()
        self.green.high()

    def run(self):
        pass

    def fast(self):
        self.red.low()
        self.yellow.high()
        self.green.low()






