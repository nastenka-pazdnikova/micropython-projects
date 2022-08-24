from pyb import Timer


class Buzzer:

    def __init__(self, pin, freq):
        self.pin = pin
        self.freq = freq

        self.timer = Timer(1, freq=self.freq)

    def beep_on(self):
        ch = self.timer.channel(1, Timer.PWM, pin=self.pin)
        ch.pulse_width_percent(50)

    def beep_off(self):
        self.timer.deinit()
