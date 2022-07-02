// C++ code
//
void setup()
{
  pinMode(A0, INPUT);
  Serial.begin(9600);
  pinMode(10, OUTPUT);
}

void loop()
{
  Serial.println(analogRead(A0));
  delay(100);
  int a = Serial.read();
  if(a >= 0) analogWrite(10,a);
  else digitalWrite(10,LOW);
}
