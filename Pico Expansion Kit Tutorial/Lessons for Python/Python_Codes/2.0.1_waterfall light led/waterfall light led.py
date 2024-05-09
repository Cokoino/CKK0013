from machine import Pin
import utime
# define led pin
leds = [Pin(i,Pin.OUT) for i in range(0,2)]
if __name__ == '__main__':
    while True:
        # waterfall led on
        for n in range(0,2):
            leds[n].value(1)
            utime.sleep_ms(200)
        # waterfall led off
        for n in range(0,2):
            leds[n].value(0)
            utime.sleep_ms(100)