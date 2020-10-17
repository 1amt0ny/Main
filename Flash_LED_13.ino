int ledPin = 13;
void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(ledPin, HIGH);
  delay(500);
  digitalWrite(ledPin, LOW);
  delay(500);
  digitalWrite(ledPin, HIGH);
  delay(100);
  digitalWrite(ledPin, LOW);
  delay(50);
  digitalWrite(ledPin, HIGH);
  delay(25);
  digitalWrite(ledPin, LOW);
  delay(25);
  digitalWrite(ledPin, HIGH);
  delay(25);
  digitalWrite(ledPin, LOW);
  delay(25);
  digitalWrite(ledPin, HIGH);
  delay(25);
  digitalWrite(ledPin, LOW);
  delay(25);
}
