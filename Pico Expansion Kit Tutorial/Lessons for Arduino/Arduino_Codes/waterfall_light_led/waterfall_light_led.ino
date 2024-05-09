char i;
void setup() {
  for(i=0;i<4;i++){
    pinMode(i,OUTPUT);
    digitalWrite(i,HIGH);
    delay(1000);
    digitalWrite(i,LOW);
    delay(1000);
    }
}
void loop() {
  //test IO port
  for(i=0;i<4;i++){
      pinMode(i,OUTPUT);
      digitalWrite(i,HIGH);
      delay(1000);
      digitalWrite(i,LOW);
      delay(1000);
    }
  }
 
