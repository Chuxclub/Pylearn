#!/usr/bin/env python3

import time
import sys
import os
import hanoi_solver


def main_title():
    print(r"__/\\\________/\\\__________________________________________________        ")
    time.sleep(0.05)
    print(r" _\/\\\_______\/\\\__________________________________________________       ")
    time.sleep(0.05)
    print(r"  _\/\\\_______\/\\\_____________________________________________/\\\_      ")
    time.sleep(0.05)
    print(r"   _\/\\\\\\\\\\\\\\\__/\\\\\\\\\_____/\\/\\\\\\_______/\\\\\____\///__     ")
    time.sleep(0.05)
    print(r"    _\/\\\/////////\\\_\////////\\\___\/\\\////\\\____/\\\///\\\___/\\\_    ")
    time.sleep(0.05)
    print(r"     _\/\\\_______\/\\\___/\\\\\\\\\\__\/\\\__\//\\\__/\\\__\//\\\_\/\\\_   ")
    time.sleep(0.05)
    print(r"      _\/\\\_______\/\\\__/\\\/////\\\__\/\\\___\/\\\_\//\\\__/\\\__\/\\\_  ")
    time.sleep(0.05)
    print(r"       _\/\\\_______\/\\\_\//\\\\\\\\/\\_\/\\\___\/\\\__\///\\\\\/___\/\\\_ ")
    time.sleep(0.05)
    print(r"        _\///________\///___\////////\//__\///____\///_____\/////_____\///__")


def main_menu():
    print("1. Play game")
    print("2. Exit")

    while True:
        user_choice = input("Make your selection: ")

        try:
            if user_choice in ("y", "Y", "1", "oui", "Oui", "yes", "Yes", "o", "O"):
                os.system("clear")
                hanoi_game()

            elif user_choice in ("n", "N", "2", "non", "Non", "non", "Non"):
                sys.exit(0)

            else:
                raise ValueError

        except ValueError:
            pass


def hanoi_game():
    solution = hanoi_solver.hanoi_solver(5)

    
    
    
print("")
main_title()
print("\n")


