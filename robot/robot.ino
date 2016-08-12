#include <Servo.h>

Servo Right;
Servo Left;


void forward() {
  Left.writeMicroseconds(1300);
  Right.writeMicroseconds(1700);
}

void backward() {
  Right.writeMicroseconds(1700);
  Left.writeMicroseconds(1300);
}
void left () {
  Right.writeMicroseconds();
}

void setup() {
  Left.attach(13);
  Right.attach(12);
  Left.writeMicroseconds(1300);
  Right.writeMicroseconds(1700);
  
  // put your setup code here, to run once:
}

void loop() {
  // put your main code here, to run repeatedly:
  forward();
  backward();
//  left();
//  right();
}
