#include<stdio.h>
#include<stdlib.h>
#include<string.h>
unsigned char input[100] = {0};
unsigned char magic[100] = "\xe4\xd0\xce\x89\xe3\xd7\xfc\xd9\xcf\x9c\x92\xc4\xa2\xff\x88\x82\xc6\x9d\xe4\xdb\xc4\xde\xe1\xd7\xf3\x8f\xc5\xce\xc8\xca\xf0\xfd\x00\x00\x00\x00\x00\x00\x00\x00";
int flag = 1;
void step1(){
    if(strlen(input) != 40){
        puts("step1 : WRONG!!!");
        flag = 0;
        system("pause");
        exit(0);
    }
    else{
        puts("step1 : OK");
    }
}
void step2(){
    if(!memcmp(input, "mssctf{", 7) && input[39] == '}'){
        puts("step2 : OK");
    }
    else{
        puts("step2 : WRONG!!!");
        flag = 0;
        system("pause");
        exit(0);
    }
}
void step3(){
    unsigned char key1[100] = "Avalon";
    unsigned char key2[100] = "Excalibur";
    unsigned char tmp1[100] = {0};
    unsigned char tmp2[100] = {0};
    for(int i=0; i<32; i++){
        tmp1[31 - i] = ~(input[i+7] ^ key1[(i)%strlen(key1)]);
    }
    for(int i=0; i<32; i++){
        tmp2[31 - i] = tmp1[i] ^ key2[i % strlen(key2)];
    }
    for(int i=0; i<32 ;i++){
        if(tmp2[i] != magic[i]){
            puts("step3 : WRONG!!!");
            flag = 0;
            system("pause");
            exit(0);
        }
    }
    puts("step3 : OK");
}
void (*funclist[3])() = {step1, step2, step3};
int main(){
    puts("[MssCTF] Welcome to MssCTF2021_Final.");
    puts("Now, please input you flag, and I will check it(I have three steps to check it):");
    scanf("%s", input);
    for(int i=0; i<3; i++){
        funclist[i]();
    }
    if(flag){
        puts("Congratulations, your capture the flag!!!");
        system("pause");
    }
}