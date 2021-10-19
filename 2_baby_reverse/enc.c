#include <stdlib.h>
#include <stdio.h>
#include <string.h>
unsigned char input[100] = {0};
int main()
{
    scanf("%s", input);
    unsigned char key1[100] = "Avalon";
    unsigned char key2[100] = "Excalibur";
    unsigned char tmp1[100] = {0};
    unsigned char tmp2[100] = {0};
    for(int i=0; i<32; i++){
        tmp1[31 - i] = ~(input[i] ^ key1[(i)%strlen(key1)]);
    }
    for(int i=0; i<32; i++){
        tmp2[31 - i] = tmp1[i] ^ key2[i % strlen(key2)];
    }
    for(int i=0; i<32; i++){
        printf("\\x%02x", tmp2[i]);
    }
}