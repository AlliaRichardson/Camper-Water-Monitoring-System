/*	relayControl.ino
*
*	Arduino Relay Shield Control from DIGITAL I/O
*	Author Howard Richardson
*	5/21/2019 Free to USE
*	For use with external audio recording.
*	For use with Raspberry Pi Pi-PlatesDAQ
*/

digital 4,5,6,7 = relay 4, 3, 2, 1

int MotorControl = 7;     // Digital Arduino Pin used to control the motor
int RelayInput = 13;      // Digital input from Raspberry Digital Output


/*	Method - loop
*
*	Description:
*		The setup routine runs once when you press reset. Declares pin to be an 
*		output, and the pin for the input control.
*	Parameters:
*		Not Applicable
*	Return:
*		Not Applicable
*/

void setup()  {
  // declare pin 7 to be an output:
  pinMode(MotorControl, OUTPUT);
  // declare pin 13 as digital input control
  pinMode(RelayInput, INPUT);
}

/*	Method - loop
*
*	Description:
*		The method sets Relay 1 to its resting state.  (Normally open contacts 
*		are open). The digital output is the inverse to the DIGITAL input of the
*		Arduino, so we read for a low from the PI. The loop routine runs over 
*		and over again forever.......................................  and ever.
*	Parameters:
*		Not Applicable
*	Return:
*		Not Applicable
*/
void loop()  {
  //Sets Relay 1 to it's resting state. 
  digitalWrite(MotorControl,LOW); 
  //while the read digital output from the relay on the Pi is low
  while (digitalRead(RelayInput)==LOW ) {  
	// NO3 and COM3 Connected (the motor is running)
  	digitalWrite(MotorControl,HIGH);
  	delay(10000); // wait 1000 milliseconds (1 second)
	// NO3 and COM3 Disconnected (the motor is not running)
  	digitalWrite(MotorControl,LOW);
  	delay(1000); // wait 1000 milliseconds (1 second)
	}
}