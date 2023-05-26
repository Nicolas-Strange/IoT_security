// Original Arduino code
int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
  delay(1000);
}

// Obfuscated Arduino code
int a = 13;

void b() {
  pinMode(a, OUTPUT);
}

void c() {
  digitalWrite(a, HIGH);
  delay(1000);
  digitalWrite(a, LOW);
  delay(1000);
}

void setup() {
  b();
}

void loop() {
  c();
}
