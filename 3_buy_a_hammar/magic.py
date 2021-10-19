# cython: language_level=3
import time
import sys
import random
import hashlib

def show(buf: str) -> None:
    print(buf)
    time.sleep(1)

def check_box(a: int) -> str :
    x = hashlib.md5(str(a).encode()).hexdigest()
    dest = ""
    for i in x:
        dest += chr(ord(i)+1)
    if a > 999999 or a < 1 :
        return "give me a number between 1 and 999999!!!"
    elif dest != "c6464bg26325::d6422437b2:fb3762c":
        return "WRONG!!!!\nTRY AGAIN!!!"
    else :
        magic = [104, 101, 96, 105, 97, 106, 41, 117, 72, 104, 73, 72, 123, 76, 104, 97, 46, 103, 74, 50, 109, 110, 77, 62, 41, 118, 72, 116, 74, 122, 121, 126, 105, 99, 110, 118, 120]
        key1 = "avyyds"
        key2 = "trackyyds"
        flag = ""
        tmp = []
        for i in range(len(magic)):
            tmp.append(magic[i] ^ ord(key2[i%len(key2)]))
        tmp = tmp[::-1]
        for i in range(len(tmp)):
            flag += chr(tmp[i] ^ ord(key1[i%len(key1)]))
        return "Cong\n" + flag

def hidden_func() -> None:
    show("QwQ, you find me.")
    show("Do you want the flag?")
    show("wwwww, I won't give it to you so easily!")
    show("How about playing another game?")
    show("yeah, a number guess game!")
    show("I have a favorite number, and it will never change.")
    show("Now, guess it!")
    show("give me a number between 1 and 999999\nAnd I will throw it to my check box\nInput the character 'q' to exit the game")
    hidden_number_guess()

def hidden_number_guess() -> None:
    while True:
        input_number = input()
        if input_number == 'q' :
            show("Bye~Bye\nYou will never capture the flag")
            time.sleep(114514)
            sys.exit()
        else:
            show(check_box(int(input_number)))

def start() -> None:
    show("[MssCTF2021_final] Welcome to my python shop!")
    menu()
    print("input 1 to buy the flag")
    print("input 2 to buy the hammer")
    print("input 3 to see how money you have")
    print("input 4 to play a game to win some money")
    print("input 9 to quit")

def menu() -> None:
    show("----- goods and costs-----")
    show("-> FLAG : 10000")
    show("-> Give a hammer to the author of the challenge : 5")

def my_python_shop() :
    money = 10
    start()
    while True:
        print("Now, please input(among 1-4, 9): ", end="")
        input_number = int(input())
        if input_number == 1:
            if money < 10000 :
                print("You don't have enough money!")
            else:
                money -= 10000
                print("flag{you are cheated}")
        if input_number == 2:
            if money < 5:
                print("You don't have enough money!")
            else:
                money -= 5
                print("You buy a hammer to hsgg. QwQ")
        if input_number == 3:
            print("Here is your money : " + str(money))
        if input_number == 4:
            print("The rules are as follows")
            print("you give me some money to guess my card is red or black, if you guess the right color, I will return you ten times money you give me")
            guess_money = int(input("input the amount of money you give me : "))
            if money - guess_money < 0 :
                print("???you don't have enough money")
            else:
                money -= guess_money
                time.sleep(1)
                print("OK, I have set the card, now guess the color of it")
                guess_color = input("input a color(red/black) : ")
                if guess_color != "red" and guess_color != "black" :
                    print("You don't obey the rules, I won't give back any money to you!!!!!")
                elif money + guess_money * 10 > 10000:
                    print("you are wrong, and you lose your money")
                else :
                    if random.randint(0,1) :
                        print("You are right! You win my money!")
                        money += guess_money * 10
                    else:
                        print("you are wrong, and you lose your money")
        if input_number == 9:
            print("Bye~Bye~")
            time.sleep(1919810)
            sys.exit()