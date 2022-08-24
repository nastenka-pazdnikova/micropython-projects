from time import sleep


class DelayService:

    def __init__(self, display, buzzer):
        self.display = display
        self.buzzer = buzzer

    def down_count(self, delay):
        while delay > 0:
            self.display.show(f"{delay}")
            sleep(0.5)
            delay = delay - 0.5

        self.display.clear()

    def down_blink_and_count(self, delay, led):

        while delay > 0:
            if led.value():
                led.low()
            else:
                led.high()

            self.display.show(f"{delay}")
            self.buzzer.beep_on()
            sleep(0.25)

            self.buzzer.beep_off()
            sleep(0.25)
            delay = delay - 0.5

        self.display.clear()
