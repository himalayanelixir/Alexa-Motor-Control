int enableA = 3;
int in1 = 4;
int in2 = 5;


void setup() {
  // put your setup code here, to run once:
  pinMode(enableA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2 ,OUTPUT);

  digitalWrite(enableA,LOW);
  digitalWrite(in1,LOW);
  digitalWrite(in2,LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  analogWrite(enableA,255);
  delay(10000);
  
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  analogWrite(enableA,255);
  delay(10000);

  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  analogWrite(enableA,255);
  delay(10000);

  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  analogWrite(enableA,255);
  delay(10000);  
}
