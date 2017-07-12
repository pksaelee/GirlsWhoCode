#include <Servo.h>

Servo servoLeft;
Servo servoRight;

void setup() {
  pinMode(13, OUTPUT);
  servoLeft.attach(13);
  servoRight.attach(12);
}

void loop() {
  servoLeft.write(0);
  servoRight.write(180);
  delay(1000);
  servoLeft.write(180);
  servoRight.write(0);
  delay(1000);
  digitalWrite(13, HIGH);   
  delay(1000);              
  digitalWrite(13, LOW);
  delay(1000);              
}
