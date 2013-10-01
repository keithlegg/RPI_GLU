
#define GPSRATE 4800



#if ARDUINO >= 100
 #include <SoftwareSerial.h>
#else
 #include <NewSoftSerial.h>
#endif

 
 
 #if ARDUINO >= 100
 SoftwareSerial gpsSerial =  SoftwareSerial(6, 7); //DRONE2 4,5 //DRONE2 3,2
#else
 NewSoftSerial gpsSerial =  NewSoftSerial(6, 7);
#endif


void setup() {
  Serial.begin(9600);
  gpsSerial.begin(GPSRATE);
}


void loop(){
  char c;
  if (gpsSerial.available()) {
    c = gpsSerial.read();
    Serial.write(c);
  }  
}


