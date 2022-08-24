// C++ code
//
#define D5 5
void setup(){ Serial.begin(9600);}
void loop()
{
  Serial.println(analogRead(A0));
  delay(100);
  int a = Serial.read();
  if(a >= 0) analogWrite(D5,a);
  else analogWrite(D5,0);
}
