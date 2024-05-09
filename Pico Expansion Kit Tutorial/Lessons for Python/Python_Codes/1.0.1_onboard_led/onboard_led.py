import machine
import utime

# Define the GPIO port of the onboard LED as a GP25 pin and set it to output mode.  
led_onboard = machine.Pin(25, machine.Pin.OUT)

while True:  
    led_onboard.value(1)    # Output high level.  
    print("Light on...")  
    utime.sleep(2)          # Delay 2s.  
    led_onboard.value(0)    # Output low level.  
    print("Light off.")  
    utime.sleep(1)          # Delay 2s
