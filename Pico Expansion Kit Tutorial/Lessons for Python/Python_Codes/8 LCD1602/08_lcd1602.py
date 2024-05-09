from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
import time


DEFAULT_I2C_ADDR = 0x27

i2c = I2C(0,sda=Pin(20),scl=Pin(21),freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

if __name__ == '__main__':
    try:
        lcd.clear()
        #lcd.putstr("Hello World! \nRaspberryPi Pico")
        lcd.putstr("Hello World! ")
        lcd.putstr("\n")
        lcd.putstr("RaspberryPi Pico")
        time.sleep(2)
        #lcd.clear()
    except KeyboardInterrupt:
        #lcd.clear()
        #lcd.backlight_off()
        pass



