#!/usr/bin/env python3

import sys
import hangman

def main_title():

    print("$$\   $$\                                                           ")      
    print("$$ |  $$ |                                                          ")      
    print("$$ |  $$ | $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$$$$$$\ ")  
    print("$$$$$$$$ | \____$$\ $$  __$$\ $$  __$$\ $$  _$$  _$$\  \____$$\ $$  __$$\ ") 
    print("$$  __$$ | $$$$$$$ |$$ |  $$ |$$ /  $$ |$$ / $$ / $$ | $$$$$$$ |$$ |  $$ |")
    print("$$ |  $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$  __$$ |$$ |  $$ |")
    print("$$ |  $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$ |$$ |  $$ |")
    print("\__|  \__| \_______|\__|  \__| \____$$ |\__| \__| \__| \_______|\__|  \__|")
    print("                              $$\   $$ |                                  ")
    print("                              \$$$$$$  |                                  ")
    print("                               \______/                                   ")


def main_menu():
    print("1. Play Hangman")
    print("2. Exit")

    while True:
        user_choice = int(input("Make your selection: "))

        try:
            if user_choice == 1:
                hangman.hangman()

            elif user_choice == 2:
                sys.exit(0)

            else:
                raise ValueError("Enter either 1 or 2")

        except ValueError:
            pass


def main():
    main_title()
    main_menu()

main()
