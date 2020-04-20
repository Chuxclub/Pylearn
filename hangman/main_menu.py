#!/usr/bin/env python3

import sys
import hangman
import time
import os


def main_title():

    print("$$\   $$\                                                           ")
    time.sleep(0.05)
    print("$$ |  $$ |                                                          ")
    time.sleep(0.05)
    print("$$ |  $$ | $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$$$$$$\ ")
    time.sleep(0.05)
    print("$$$$$$$$ | \____$$\ $$  __$$\ $$  __$$\ $$  _$$  _$$\  \____$$\ $$  __$$\ ")
    time.sleep(0.05)
    print("$$  __$$ | $$$$$$$ |$$ |  $$ |$$ /  $$ |$$ / $$ / $$ | $$$$$$$ |$$ |  $$ |")
    time.sleep(0.05)
    print("$$ |  $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$  __$$ |$$ |  $$ |")
    time.sleep(0.05)
    print("$$ |  $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$ |$$ |  $$ |")
    time.sleep(0.05)
    print("\__|  \__| \_______|\__|  \__| \____$$ |\__| \__| \__| \_______|\__|  \__|")
    time.sleep(0.05)
    print("                              $$\   $$ |                                  ")
    time.sleep(0.05)
    print("                              \$$$$$$  |                                  ")
    time.sleep(0.05)
    print("                               \______/                                   ")


def main_menu():
    print("1. Play Hangman")
    print("2. Exit")
    print("")

    while True:
        user_choice = input("Make your selection: ")

        try:
            if user_choice in ("1", "o", "O", "y", "Y",
                               "oui", "yes", "Oui", "Yes"):
                os.system("clear")
                hangman.hangman()

            elif user_choice in ("2", "n", "N", "non", "no", "Non", "No"):
                os.system("clear")
                sys.exit(0)

            else:
                raise ValueError("Enter either 1 or 2")

        except ValueError:
            pass


def main():
    print("\n")
    main_title()
    print("\n")
    time.sleep(1)
    main_menu()


main()
