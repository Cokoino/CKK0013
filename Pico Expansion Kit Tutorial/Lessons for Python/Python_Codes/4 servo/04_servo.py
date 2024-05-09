from machine import Timer,Pin, PWM, ADC
# from machine import time_pulse_us
import time, array
import math

# mapping function
def map(x,in_max, in_min, out_max, out_min):
    return (x - in_min)/(in_max - in_min)*(out_max - out_min) + out_min

'''
PERIOD = ffff = 65535
freq = 50
'''
class Servo():
    pwm_max = 2500
    pwm_min = 500
    period = 65535 # oxFFFF
    
    def __init__(self):
        pass
    
    
    def  set_angle(self, pin, angle):  # Pin:Servo GPIO pins, angle:Servo rotation angle -90~90.
        self.servo = PWM(Pin(pin, Pin.OUT))
        self.servo.freq(50) # Set servo Freq.
        if angle < -90:
            angle = 90
        if angle > 90:
            angle = 90
        high_level_time = map(angle, 90, -90, self.pwm_max, self.pwm_min)
        # Servo duty cycle value.
        duty_cycle_value = int((high_level_time/20000)*self.period)
        self.servo.duty_u16(duty_cycle_value)
        
if __name__ == '__main__':
    while True:
        servo = Servo()
        servo.set_angle(7, 90)  # Rotate to 90 degrees.
        time.sleep(1)           # delay 1s.
        servo.set_angle(7, -90) # Rotate to -90 degrees.
        time.sleep(1)
            
    