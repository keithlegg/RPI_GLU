int a1 = 8;
int a2 = 9;
int b1 = 10;
int b2 = 11;

int led = 13;

int delval = 200;
String inputString = "";   
boolean stringComplete = false;

boolean enable_motor = false;


void setup() {                
  pinMode(a1, OUTPUT);     
  pinMode(a2, OUTPUT); 
  pinMode(b1, OUTPUT); 
  pinMode(b2, OUTPUT); 

  Serial.begin(9600);
  inputString.reserve(200);
  pinMode(led, OUTPUT);   
}

void clear_all(){
  digitalWrite(a1, LOW);   
  digitalWrite(a2, LOW); 
  digitalWrite(b1, LOW);   
  digitalWrite(b2, LOW); 

}


void run_stepper() {
  clear_all();
  digitalWrite(a1, HIGH);   
  delay(delval); 
  clear_all();  
  digitalWrite(b1, HIGH);   
  delay(delval);     
  clear_all();
  digitalWrite(a2, HIGH); 
  delay(delval);        
  clear_all();
  digitalWrite(b2, HIGH);   
  delay(delval);  
  clear_all();  
}


void loop() {
  
  if(enable_motor){
    run_stepper(); //RUN THE STEPPER MOTOR
  }
  
  if (stringComplete) {
    Serial.println(inputString); 
    inputString = "";
    stringComplete = false;
  }
}


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
    
    
    //flash pin 13 when receiving data   
    if (inChar == 'z') {
       enable_motor =true;
    } 
  
    //flash pin 13 when receiving data   
    if (inChar == 'x') {
       enable_motor =false;
    } 
    
    //flash pin 13 when receiving data   
    if (inChar == 'a') {
      digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
      delval=delval+10;
      //delay(1000);               // wait for a second
    } 
     
    //flash pin 13 when receiving data
    if (inChar == 'b') {
      digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
      delval=delval-10;
      //delay(1000);               // wait for a second
    } 
    
    digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  
  }
}



