from machine import Timer,Pin, PWM, ADC
#from machine import time_pulse_us
import time, array
import math

class Ultrasonic():
    # Define output(trig) and input(echo) pins.
    def __init__(self, trig, echo):
        self._trig = Pin(trig, Pin.OUT)
        self._echo = Pin(echo, Pin.IN)
    
    def get_distance(self):
        # Generate 10us square wave.
        self._trig.low()
        time.sleep_us(2)
        self._trig.high()
        time.sleep_us(10)
        self._trig.low()
        while self._echo.value() == 0:
            start = time.ticks_us()
        while self._echo.value() == 1:
            end = time.ticks_us()
        dis = (end - start) * 0.0343 / 2
        # round to two decimal places.
        return round(dis, 2)
    
if __name__ == '__main__':
    # Ultrasonic pins. trig:GPIO1, echo:GPIO0
    ultrasonic = Ultrasonic(1,0)
    while True:
        value = ultrasonic.get_distance()
        print("Distance: {:.2f}cm" .format(value))
        time.sleep(1)
        