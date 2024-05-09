from machine import Pin, PWM
import time

class Buzzer():
    def __init__(self):
        self._buzzer = PWM(Pin(16, Pin.OUT))

    def playtone(self, frequency):
        self._buzzer.duty_u16(60000)
        self._buzzer.freq(frequency)
        
    def sound(self):
        buzzer.playtone(1500)
        

    def bequiet(self):
        self._buzzer.duty_u16(0)

if __name__ == '__main__':
    buzzer = Buzzer()
    try:
        while True:
            buzzer.playtone(1500)
            time.sleep(1)
            buzzer.playtone(1200)
            time.sleep(1)
    except KeyboardInterrupt:
        buzzer.bequiet()