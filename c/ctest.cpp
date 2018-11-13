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

int SWITCHES[8][3] = {{0,0,0},{0,0,1},{0,1,0},{0,1,1},{1,0,0},{1,0,1},{1,1,0},{1,1,1}};

int COLOURS[8][3] = {{0,0,0},{0,0,100},{0,100,0},{0,100,100},{100,0,0},{100,0,100},{100,100,0},{100,100,100}};

void turnOff(void){
    softPwmWrite(R,0);
    softPwmWrite(G,0);
    softPwmWrite(B,0);
}

void writeColours(int[3]  RGB){
    softPwmWrite(R,RGB[0]);
    softPwmWrite(G,RGB[2]);
    softPwmWrite(B,RGB[1]);
}

void testhsv(void){
    hsv a = {1.0,1.0,1.0};

    for(int i =0; i< 361;i++){
        a.h=i;
        rgb b = hsv2rgb(a);
        //cout<<b.r<<","<<b.g<<","<<b.b<<endl;
        writeColours([b.r*100, b.g*100,b.b*100])
        delay(15);
    }
}

void test4051(void){
    for (int i=0; i<8; i++){
        digitalWrite(S0Pin, SWITCHES[i][0]);
        digitalWrite(S1Pin, SWITCHES[i][1]);
        digitalWrite(S2Pin, SWITCHES[i][2]);
        delay(1);
    }
}

void testDifferent(void){
    for (int i=0; i<8; i++){
        writeColours(COLOURS[i]);
        digitalWrite(S0Pin, SWITCHES[i][0]);
        digitalWrite(S1Pin, SWITCHES[i][1]);
        digitalWrite(S2Pin, SWITCHES[i][2]);
        delay(1);
    }
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

pinMode(S0Pin,OUTPUT);
pinMode(S1Pin,OUTPUT);
pinMode(S2Pin,OUTPUT);

softPwmCreate(R,0,100);
softPwmCreate(G,0,100);
softPwmCreate(B,0,100);

    //testColors();
while(1){
    test4051();
}
return 0;
}
