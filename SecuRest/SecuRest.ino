#include<Servo.h>

int distance = 0;
int sPin = 4;
int iter = 0;
long duration = 0;

Servo s1;

void setup() {
  pinMode(2, INPUT);
  pinMode(3, OUTPUT);
  s1.attach(sPin);
  s1.write(0);
  Serial.begin(9600);
}

void loop() {
  iter++;
  digitalWrite(3, LOW);
  delayMicroseconds(2);
  digitalWrite(3, HIGH);
  delayMicroseconds(10);
  digitalWrite(3, LOW);
  duration = pulseIn(2, HIGH);
  distance = duration * 0.034 / 2;
  Serial.println(distance);
  int move_signal = Serial.read();
  if (Serial.available()) {
    Serial.println(int(Serial.read()));
    if (move_signal == 77) {
      s1.write(0);
      delay(1000);
      s1.write(40);
      delay(1000);
      s1.write(80);
      delay(1000);
      s1.write(120);
      delay(1000);
      s1.write(160);
      delay(1000);
      s1.write(0);
      delay(1000);
      s1.write(90);
    }
  }
}
