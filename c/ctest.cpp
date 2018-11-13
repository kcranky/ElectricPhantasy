#include<iostream>
#include<wiringPi.h>
#include <softPwm.h>
#include "hsvtorgb.h"

using namespace std;

#define R 23
#define G 24
#define B 25

#define S0Pin 27
#define S1Pin 28
#define S2Pin 29

void cycleColors(void){
    for(int r=1; r<256; r++){
        for(int g=1; g<256; g++){
            for(int b=1; b<256; b++){
                softPwmWrite(B,b);
                softPwmWrite(R,r);
                softPwmWrite(G,g);
                delay(50);
            }
        }
    }
    delay(1000);
}


void hsvtest(void){
    hsv a = {1.0,1.0,1.0};

    for(int i =0; i< 361;i++){
        a.h=i;
        rgb b = hsv2rgb(a);
        cout<<b.r<<","<<b.g<<","<<b.b<<endl;
        softPwmWrite(R, b.r*100);
        softPwmWrite(G, b.g*100);
        softPwmWrite(B, b.b*100);
        delay(6);
    }
}

void turnOff(void){
    softPwmWrite(R,0);
    softPwmWrite(G,0);
    softPwmWrite(B,0);
}

void testColors(void){
    int i = 0;
    turnOff();

    for (i=0; i<101;i++){
        softPwmWrite(R,i);
        delay(20);
    }
    turnOff();
    delay(1000);
    for(i=0; i<101; i++){
        softPwmWrite(G,i);
        delay(20);
    }
    turnOff();
    delay(1000);
    for(i=0; i<101;i++){
        softPwmWrite(B,i);
        delay(20);
    }
    turnOff();
    delay(1000);
}


 int main(void)
 {

 if(wiringPiSetup()==-1)
{
    cout<<"Setup wiring pi failed\n";
    return 1;
}

cout<<"We're here!\n";

pinMode(R,OUTPUT);
pinMode(B,OUTPUT);
pinMode(G,OUTPUT);

//pinMode(S0Pin,OUTPUT);
//pinMode(S1Pin,OUTPUT);
//pinMode(S2Pin,OUTPUT);

softPwmCreate(R,0,256);
softPwmCreate(G,0,256);
softPwmCreate(B,0,256);

    //testColors();
    hsvtest();

return 0;
}
