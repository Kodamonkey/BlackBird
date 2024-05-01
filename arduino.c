#define LED_pin 13
#define LED_error_pin 8

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_pin, OUTPUT);
  //pinMode(LED_error_pin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  //String msg = "STATIC";
  if (Serial.available() > 0) {
    String msg = Serial.readString();
    if (msg == ".") {
      digitalWrite(LED_pin, HIGH);
      delay(500);
      digitalWrite(LED_pin, LOW);
      delay(200);
    }
    else if (msg == "-") {
      digitalWrite(LED_pin, HIGH);
      delay(800);
      digitalWrite(LED_pin, LOW);
      delay(200);
    }
    else if (msg == "/")
      digitalWrite(LED_pin, LOW);
      delay(1000);
  }
}