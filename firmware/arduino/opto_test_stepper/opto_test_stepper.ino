int a1 = 8;
int a2 = 9;
int b1 = 10;
int b2 = 11;

int delval = 100;

// the setup routine runs once when you press reset:
void setup() {                
  pinMode(a1, OUTPUT);     
  pinMode(a2, OUTPUT); 
  pinMode(b1, OUTPUT); 
  pinMode(b2, OUTPUT);   
}

void clear_all(){
  digitalWrite(a1, LOW);   
  digitalWrite(a2, LOW); 
  digitalWrite(b1, LOW);   
  digitalWrite(b2, LOW); 

}


// the loop routine runs over and over again forever:
void loop() {
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
