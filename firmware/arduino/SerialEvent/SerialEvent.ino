String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

int led = 13;

void setup() {

  Serial.begin(9600);
  pinMode(led, OUTPUT);  
  inputString.reserve(200);
}

void loop() {
  if (stringComplete) {
    Serial.println(inputString); 
    inputString = "";
    stringComplete = false;
  }
}

/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read(); 
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    } 
    
    if (inChar == 'a') {
      digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
      delay(1000);               // wait for a second
    } 
    digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  
  }
}


