import array, time
from machine import Pin
import rp2


@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812_led():
    T1 = 2
    T2 = 5
    T3 = 1
    
    wrap_target() # .side()Specifies where the program continues execution.
    label("bitloop")
    out(x, 1).side(0)[T3 - 1] # []Delay a certain number of cycles after executing the instruction.
    jmp(not_x, "do_zero").side(1)[T1 - 1]
    jmp("bitloop").side(1)[T2 - 1]
    label("do_zero")
    nop().side(0)[T2 - 1]
    wrap()
 
class WS2812():
    def __init__(self):
        # Configure the number of WS2812 LEDs, pins and brightness.
        # define WS2812/SK6812(color_led) LED number, pin and brightness
        self._led_num = 4 #  LED number
        self._pin = 3    # GPIO11
        self.brightness_value = 0.2  # light brightness. The value range is 0~1.
        # Create the StateMachine with the ws2812 program, outputting on Pin(PIN_NUM).
        self.sm = rp2.StateMachine(0, ws2812_led, freq=8_000_000, sideset_base=Pin(self._pin))
        # Start the StateMachine, it will wait for data on its FIFO.
        self.sm.active(1)
        # Display a pattern on the LEDs via an array of LED RGB values.
        self.ar = array.array("I", [0 for _ in range(self._led_num)])
        
    def pixels_show(self):
        dimmer_ar = array.array("I", [0 for _ in range(self._led_num)])
        for i,c in enumerate(self.ar):
            r = int(((c >> 8) & 0xFF))
            g = int(((c >> 16) & 0xFF))
            b = int((c & 0xFF))
            dimmer_ar[i] = (g<<16) + (r<<8) + b
        self.sm.put(dimmer_ar, 8)
        time.sleep_ms(10)

    # Set multiple colors
    # Set the color of the specified ws2812.
    def pixels_set(self,i, color):
        R = round(color[0] * self.brightness_value)
        G = round(color[1] * self.brightness_value)
        B = round(color[2] * self.brightness_value)
        self.ar[i] = (G<<16) + (R<<8) + B
        self.pixels_show()
        
    # Set the color of all ws2812 led.
    def pixels_fill(self,color):
        for i in range(len(self.ar)):
            self.pixels_set(i, color)
    
    # Set a single color.
    def set_color(self,i,R,G,B):
        
        R = round(R * self.brightness_value)
        G = round(G * self.brightness_value)
        B = round(B * self.brightness_value)
        self.ar[i] = (G<<16) + (R<<8) + B
        self.pixels_show()
    
    def set_color_all(self, R, G, B):
        for i in range(len(self.ar)):
            self.set_color(i, R, G, B)
    
    # Adjust the brightness, the value range is 0-1, the default value is 0.2
    def brightness(self, brightness = None):
        if brightness == None:
            return self.brightness_value
        else:
            if (brightness < 0):
                brightness = 0
        if (brightness > 1):
            brightness = 1
        self.brightness_value = brightness
        
    # breathing light.
    def breath(self, R, G, B):
        breathSteps = 10
        for i in range(1,breathSteps):
            Breath_R = round(R*i/breathSteps)
            Breath_G = round(G*i/breathSteps)
            Breath_B = round(B*i/breathSteps)
            self.set_color_all(Breath_R, Breath_G, Breath_B)
            
            #self.pixels_show()
            #self.setColor(self.colorBreathR*i/self.breathSteps, self.colorBreathG*i/self.breathSteps, self.colorBreathB*i/self.breathSteps)
            time.sleep(0.06)
        for i in range(1,breathSteps):
            Breath_R = round(R-R*i/breathSteps)
            Breath_G = round(G-G*i/breathSteps)
            Breath_B = round(B-B*i/breathSteps)
            self.set_color_all(Breath_R, Breath_G, Breath_B)
            #self.pixels_show()
            
            #self.setColor(self.colorBreathR-(self.colorBreathR*i/self.breathSteps), self.colorBreathG-(self.colorBreathG*i/self.breathSteps), self.colorBreathB-(self.colorBreathB*i/self.breathSteps))
            time.sleep(0.06)
    
    # Lights off
    def stop(self):
        robot_light.set_color_all(0,0,0)
        
    def test_multiple_colors(self):
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        YELLOW = (255, 150, 0)
        GREEN = (0, 255, 0)
        CYAN = (0, 255, 255)
        BLUE = (0, 0, 255)
        PURPLE = (180, 0, 255)
        WHITE = (255, 255, 255)
        COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)
        for color in COLORS:
            self.pixels_fill(color)
            #self.pixels_show()
            time.sleep(2)


if __name__ == '__main__':
    
    robot_light = WS2812()
    try:
        while True:
            # test color multiple colors.
            robot_light.test_multiple_colors()
            
            # set a single color.
            #robot_light.set_color_all(255,0,0)
            
            # test breath led.
            #robot_light.breath(250,0,0)
            
            # test adjust the brightness of the lights.
            #robot_light.brightness(0.03)
    
    except KeyboardInterrupt:     # Stop the program, the light goes out.
        robot_light.stop()

