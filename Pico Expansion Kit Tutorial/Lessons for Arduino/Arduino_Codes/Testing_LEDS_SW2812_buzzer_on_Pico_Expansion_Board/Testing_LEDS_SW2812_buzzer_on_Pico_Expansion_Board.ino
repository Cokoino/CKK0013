/**********************************************************************
* Filename    : Testing_LEDS_SW2812_buzzer_on_Pico_Expansion_Board.ino
* Product     : Cokoino Pico_Extension_Board Kit
* Description : Testing_LEDS_SW2812_buzzer
* Auther      : www.cokoino.com
* Modification: 2022/07/06
**********************************************************************/
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h> // Required for 16 MHz Adafruit Trinket
#endif
#define LED_PIN    3  // Which pin on the Arduino is connected to the NeoPixels?
#define LED_COUNT 4  // Which pin on the Arduino is connected to the NeoPixels?
#define Led_delay 100
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

char Buzzer_Pin = 16;
int LED1_Pin = 15;
int LED2_Pin = 9;
int LED3_Pin = 18;

void setup() 
{
  #if defined(__AVR_ATtiny85__) && (F_CPU == 16000000)
      clock_prescale_set(clock_div_1);
  #endif
  // END of Trinket-specific code.
  strip.begin();           // INITIALIZE NeoPixel strip object (REQUIRED)
  strip.show();            // Turn OFF all pixels ASAP
  strip.setBrightness(50); // Set BRIGHTNESS to about 1/5 (max = 255)
  Serial.begin(9600);
}

void loop() 
{
  SW2812_Test();
  Buzz_Test();
  LED_Test();
}

void Buzz_Test()
{
  for (char i = 0; i < 80; i++)
  {
    digitalWrite(Buzzer_Pin,HIGH);
    delay(1);
    digitalWrite(Buzzer_Pin,LOW);
    delay(1);
  }
  for (char i = 0; i < 100; i ++)
  {
    digitalWrite(Buzzer_Pin,HIGH);
    delay(2);
    digitalWrite(Buzzer_Pin,LOW);
    delay(2);
  }
}
void  LED_Test()
{
  pinMode( LED1_Pin,OUTPUT);
  pinMode( LED2_Pin,OUTPUT);
  pinMode( LED3_Pin,OUTPUT);
  digitalWrite(LED1_Pin,HIGH);
  digitalWrite(LED2_Pin,HIGH);
  digitalWrite(LED3_Pin,HIGH); 
  delay(1000);
  digitalWrite(LED1_Pin,LOW);
  digitalWrite(LED2_Pin,LOW);
  digitalWrite(LED3_Pin,LOW); 
}
void SW2812_Test()
{
  colorWipe(strip.Color(255,   0,    0), Led_delay); // Red
  colorWipe(strip.Color(  0, 255,    0), Led_delay); // Green
  colorWipe(strip.Color(  0,   0,  255), Led_delay); // Blue
  colorWipe(strip.Color(  255,255, 255), Led_delay); // While
  //rainbow(10);             // Flowing rainbow cycle along the whole strip
  //theaterChaseRainbow(50); // Rainbow-enhanced theaterChase variant
}

void colorWipe(uint32_t color, int wait) {
  for(int i=0; i<strip.numPixels(); i++) { // For each pixel in strip...
    strip.setPixelColor(i, color);         //  Set pixel's color (in RAM)
    strip.show();                          //  Update strip to match
    delay(wait);                           //  Pause for a moment
  }
}

void theaterChase(uint32_t color, int wait) 
{
  for(int a=0; a<10; a++) {  // Repeat 10 times...
    for(int b=0; b<3; b++) { //  'b' counts from 0 to 2...
      strip.clear();         //   Set all pixels in RAM to 0 (off)
      // 'c' counts up from 'b' to end of strip in steps of 3...
      for(int c=b; c<strip.numPixels(); c += 3) {
        strip.setPixelColor(c, color); // Set pixel 'c' to value 'color'
      }
      strip.show(); // Update strip with new contents
      delay(wait);  // Pause for a moment
    }
  }
}

void rainbow(int wait) 
{
  for(long firstPixelHue = 0; firstPixelHue < 5*65536; firstPixelHue += 256)
  {
    strip.rainbow(firstPixelHue);
    strip.show(); // Update strip with new contents
    delay(wait);  // Pause for a moment
  }
}

void theaterChaseRainbow(int wait) 
{
  int firstPixelHue = 0;     // First pixel starts at red (hue 0)
  for(int a=0; a<30; a++) {  // Repeat 30 times...
    for(int b=0; b<3; b++) { //  'b' counts from 0 to 2...
      strip.clear();         //   Set all pixels in RAM to 0 (off)
      for(int c=b; c<strip.numPixels(); c += 3)
      {
        int      hue   = firstPixelHue + c * 65536L / strip.numPixels();
        uint32_t color = strip.gamma32(strip.ColorHSV(hue)); // hue -> RGB
        strip.setPixelColor(c, color); // Set pixel 'c' to value 'color'
      }
      strip.show();                // Update strip with new contents
      delay(wait);                 // Pause for a moment
      firstPixelHue += 65536 / 90; // One cycle of color wheel over 90 frames
    }
  }
}
