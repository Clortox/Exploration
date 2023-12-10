///////////////////////////////////////////////////////////////////////////////////////////////////
// Tyler Perkins
// 12-30-20
// Testing command line audio

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>

int main(int argc, char** argv){
    if(argc != 1){
        printf("Usage: %s\n", argv[0]);
        return -1;
    }

    //sawtooth wave
    for(int t=0, osc=0; t<8000; t++, osc += 14){
        putchar(osc);
    }

    //square wave
    for(int t=0, osc=0; t<8000; t++, osc += 14){
        putchar(osc & 0x80);
    }

    //sine wave
    for(int t=0, osc=0; t<8000; t++, osc += 14){
        putchar(127 * sin(osc/255.0*2*3.1415) + 128);
    }

    
    /* kinda bass guitar?
     *
     * The idea here is an array full of random data, with 
     * an array size equal to the period of the wave
     * (for 440 its ~18) then loop the array. 
     * Then we average out the current value and next one
     * Till we get a faded noise to silence
     *
     * Pretty cool ngl
     */

    unsigned char a[18];

    //init the array with random data
    FILE *fp;
    fp = fopen("/dev/random", "r");
    if(fp == NULL){
        printf("Couldnt open random stream!\n");
        return -1;
    }
    if(fgets(a,sizeof(a),fp)==NULL){
        printf("Failed to read the random stream!\n");
        return -1;
    }
    fclose(fp);

    //play the bass guitar
    for(int t=0;t<8000;t++){
        int i = t % sizeof(a);
        int j = (t+1) % sizeof(a);
        putchar(a[i] = (a[i] + a[j])/2);
    }

    return 0;
}
