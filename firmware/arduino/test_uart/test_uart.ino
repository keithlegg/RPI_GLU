
int led = 13;

// the setup routine runs once when you press reset:
void setup() {                
  Serial.begin(115200);
   
  pinMode(led, OUTPUT);     
}

// the loop routine runs over and over again forever:
void loop() {
  //if (Serial.available()) {
    //Serial.print(0x41); //65 ?
    Serial.print("a"); 

    Serial.print("b"); 

    Serial.print("c");     
  //}
   
  //digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  //delay(100);               // wait for a second
  //digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  //delay(100);               // wait for a second
}
