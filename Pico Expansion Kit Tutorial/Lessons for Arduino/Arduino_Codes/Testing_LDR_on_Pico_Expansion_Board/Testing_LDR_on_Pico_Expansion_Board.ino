/**********************************************************************
* Filename    : LDR Test.ino
* Product     : Cokoino Pico_Expansion_Board Kit
* Description : Testing LDR control LED
* Auther      : www.cokoino.com
* Modification: 2022/07/06
**********************************************************************/
int Buzzer_Pin=16;//Buzzer connect to Pico GP16
int led_Pin=25;//LED connect to Pico GP16
int LDR_Pin=27;//LDR connect to Pico GP16
int val=0;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(led_Pin,OUTPUT);
pinMode(LDR_Pin,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
int LDR_Value=analogRead(27);//Read value of LDR sensor on the Pico Extension Board
Serial.println(LDR_Value);//print the value on the serial monitor,value(min)=0,value(max)=1024
if(LDR_Value>=200)//Set instruction condition values,you can set it between 0~1024 as you want
{
 Buzz_Test();// Buzz working
 LED_Test();//LED on
}
else
{
digitalWrite(led_Pin,LOW);//led off
}
delay(1000);
}

void Buzz_Test()
{
  for (char i = 0; i < 80; i++)
  {
    digitalWrite(Buzzer_Pin,HIGH);
    delay(2);
    digitalWrite(Buzzer_Pin,LOW);
    delay(2);
  }
  for (char i = 0; i < 100; i++)
  {
    digitalWrite(Buzzer_Pin,HIGH);
    delay(1);
    digitalWrite(Buzzer_Pin,LOW);
    delay(1);
  }
}
void LED_Test()
{
    digitalWrite(led_Pin,HIGH); 
}
