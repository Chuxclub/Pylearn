#!/usr/bin/env python3

import time
import sys
import os
import hanoi_solver
import hanoi_ascii
import towers_manipulation


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
    print("")

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


def translate_tower_index(user_input):

    try:

        return {"A": 1,
                "a": 1,
                "1": 1,
                "B": 2,
                "b": 2,
                "2": 2,
                "C": 3,
                "c": 3,
                "3": 3}[user_input]

    except KeyError:
        pass


def remove_whitespace(user_input):

    while " " in user_input:
        user_input = user_input.replace(" ", "")

    return user_input


def hanoi_game():
    tower1 = hanoi_solver.create_hanoi_tower(2)
    tower2 = [0, 0]
    tower3 = [0, 0]
    towers = [tower1, tower2, tower3]
    # solution = hanoi_solver.hanoi_solver(5)

    os.system("clear")
    print("\n")
    hanoi_ascii.print_towers(towers)
    print("\n")

    while True:
        user_input = input("Enter your movement: ")

        try:
            if not user_input:
                raise ValueError

            user_input = remove_whitespace(user_input)
            res_list = [user_input[0], translate_tower_index(user_input[1])]

            if int(res_list[0]) in range(1, len(towers)+1) and res_list[1] in (1, 2, 3):
                towers = towers_manipulation.move_ring(res_list, towers)
                os.system("clear")
                hanoi_ascii.print_towers(towers)
                print("\n")

            else:
                raise ValueError

        except ValueError:
            print("Invalid movement!")


print("")
main_title()
print("\n")
main_menu()
print("\n")
