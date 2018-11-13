#include<iostream>
#include<wiringPi.h>
#include <softPwm.h>

using namespace std;

#define  RedPin 23
#define  GreenPin 24
#define  BluePin 25

#define S0Pin 27
#define S1Pin 28
#define S2Pin 29


 int main(void)
 {

 if(wiringPiSetup()==-1)
{
    cout<<"Setup wiring pi failed\n";
    return 1;
}

cout<<"We're here!\n";

pinMode(RedPin,OUTPUT);
pinMode(BluePin,OUTPUT);
pinMode(GreenPin,OUTPUT);

pinMode(S1Pin,OUTPUT);
pinMode(S1Pin,OUTPUT);
pinMode(S2Pin,OUTPUT);

softPwmCreate(RedPin,0,100);
softPwmCreate(BluePin,0,100);
softPwmCreate(GreenPin,0,100);

while(1)
{
    cout<<"RED ON\n";
    softPwmWrite(RedPin, 100);
    delay(500);

    cout<<"BLUE ON\n";
    softPwmWrite(BluePin,30);
    softPwmWrite(RedPin, 0);
    delay(500);

    cout<<"GREEN ON\n";
    softPwmWrite(BluePin, 0);
    softPwmWrite(GreenPin, 5);
    delay(500);

    softPwmWrite(GreenPin,0);
}
return 0;
}
