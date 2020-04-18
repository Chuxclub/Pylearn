#!/usr/bin/env python

import sys
import random
import time

random.seed

def main_title():

    print(" /$$$$$$$                      /$$                 /$$$$$$$                                                /$$$$$$  /$$    ")                                             
    print("| $$__  $$                    | $$                | $$__  $$                                              /$$__  $$|__/   ")                                              
    print("| $$  \ $$  /$$$$$$   /$$$$$$$| $$   /$$          | $$  \ $$ /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$       | $$  \__/ /$$  /$$$$$$$ /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$$ ")
    print("| $$$$$$$/ /$$__  $$ /$$_____/| $$  /$$/          | $$$$$$$/|____  $$ /$$__  $$ /$$__  $$ /$$__  $$      | $$      | $$ /$$_____//$$_____/ /$$__  $$ /$$__  $$ /$$_____/ ")
    print("| $$__  $$| $$  \ $$| $$      | $$$$$$/           | $$____/  /$$$$$$$| $$  \ $$| $$$$$$$$| $$  \__/      | $$      | $$|  $$$$$$|  $$$$$$ | $$  \ $$| $$  \__/|  $$$$$$ ")
    print("| $$  \ $$| $$  | $$| $$      | $$_  $$           | $$      /$$__  $$| $$  | $$| $$_____/| $$            | $$    $$| $$ \____  $$\____  $$| $$  | $$| $$       \____  $$ ")
    print("| $$  | $$|  $$$$$$/|  $$$$$$$| $$ \  $$ /$$      | $$     |  $$$$$$$| $$$$$$$/|  $$$$$$$| $$ /$$        |  $$$$$$/| $$ /$$$$$$$//$$$$$$$/|  $$$$$$/| $$       /$$$$$$$/ ")
    print("|__/  |__/ \______/  \_______/|__/  \__/| $/      |__/      \_______/| $$____/  \_______/|__/| $/         \______/ |__/|_______/|_______/  \______/ |__/      |_______/ ")
    print("                                        |_/                          | $$                    |_/                   ")                                                     
    print("                                                                     | $$                                                             ")                                  
    print("                                                                     |__/                                                             ")                                  

def main_menu():
    print("1. Enter Game")
    print("2. Exit")
    print("\n")
       
    valid = False

    while valid == False:
        choice = int(input("Enter your selection: "))
        
        if choice == 1:
            valid = True
            rpc_game()

        elif choice == 2:
            sys.exit(0)

        else:
            valid = False

def bot_rpc():
    return random.choice(['r', 'p', 'c'])
    
def shifumi(user_score):
    bot = bot_rpc()
    user_rpc = input("\nMake your choice human: ")

    if user_rpc == bot_rpc:
        print("Draw!")
        return user_score

    elif (user_rpc == 'r' and bot == 'c') or (user_rpc == 'p' and bot == 'r') or (user_rpc == 'c' and bot == 'p'):
        print("You win!")
        user_score += 1
        return user_score

    else:
        print("You lose!")
        return user_score
    

def rpc_game():
    
    go_on = True

    while go_on:
        print("\n\n=========== Game On! ===========")
        user_score = 0
        
        for i in range(0, 3):
            user_score = shifumi(user_score)
    
        if user_score > 1:
            print("\nYou're the winner... How is it that I, a fantastic machine, lost against you...")

        else:
            print("\nI win, you pathetic human")
                
        go_on = int(input("Try again? "))
        print("\n================================\n")

def game():
    main_title()
    main_menu()

print("\n")
game()
print("\n")
