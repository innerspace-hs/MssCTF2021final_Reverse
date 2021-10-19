#include<stdio.h>
#include<string.h>
#include<windows.h>

char input[100]={0};
char en_flag[100]="mssctf{3be4059d92bcf9e14d9b14da1f04c9fd}";
int check(){
    if(strlen(input) != 40){
        return 0;
    }
    if(!strcmp(input,en_flag)){
        return 1;
    }
    else {
        return 0;
    }
}
int main(){
    printf("[gift] Welcome to mssctf2021.\n");
    printf("Here is a gift for you~~~\n");
    printf("But I must check your flag first.\n");
    printf("Please input your flag and I will check it!\n");
    printf("input: ");
    scanf("%s",input);
    if(check()){
        printf("Congratulations!!!\n");
        printf("Your flag is right!!!\n");
        printf("And you can get the score of this challenge\n");
        printf("And this is also my gift for you~~~\n");
        printf("Have Fun!");
        Sleep(0xdeadbeef);
    }
    else{
        printf("Try again!");
        Sleep(0xdeadbeef);
    }
}