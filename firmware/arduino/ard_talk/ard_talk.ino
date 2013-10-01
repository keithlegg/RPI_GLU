


int incomingByte = 0;   // for incoming serial data

void setup() {
        Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
}

void loop() {

        // send data only when you receive data:
        if (Serial.available() > 0) {
                // read the incoming byte:
                incomingByte = Serial.read();

                // say what you got:
                Serial.print("I received: ");
                Serial.println(incomingByte, DEC);
        }
}


/*
int led = 13;

// the setup routine runs once when you press reset:
void setup() {                
  Serial.begin(9600);
   
  pinMode(led, OUTPUT);     
}

// the loop routine runs over and over again forever:
void loop() {

    digitalWrite(led, HIGH);
    Serial.print("abcde"); 

    //delay(1000);  
    digitalWrite(led, LOW);    
    //delay(1000);
 
  //   // turn the LED on (HIGH is the voltage level)
  //delay(100);               // wait for a second
  //digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  //delay(100);               // wait for a second
}
*/

