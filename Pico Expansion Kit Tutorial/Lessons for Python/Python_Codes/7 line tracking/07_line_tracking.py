import time
from machine import Pin

# Define three infrared ray tracking interface pins.
ir_left = Pin(10, Pin.IN)
ir_middle = Pin(11, Pin.IN)
ir_right = Pin(12, Pin.IN)

def get_ir_value():
    return [ir_left.value(),ir_middle.value() ,ir_right.value()]

def test():
    value = get_ir_value()
    print("left: {}, middle: {}, right: {}" .format(value[0], value[1], value[2]))

if   __name__ == '__main__':
    while True:
        test()
        time.sleep_ms(300)
        
    '''
    #lcd.clear()
    #lcd.putstr("Tracking now!")
    # lcd.putstr("L="+str(ir_left.value())+"M="+str(ir_middle.value())+"R="+str(ir_right.value()))

    if(ir_left.value() == 0):
        lcd.move_to(0,1)
        # time.sleep(0.01);
        lcd.putstr("L="+str(ir_left.value()))
    
    if(ir_middle.value() == 0):
        lcd.move_to(6,1)
        lcd.putstr("M="+str(ir_middle.value()))
    
    if(ir_right.value() == 0):
        lcd.move_to(13,1)
        lcd.putstr("R="+str(ir_right.value()))
     '''
 
