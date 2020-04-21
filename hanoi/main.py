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
    print("1. Play it super easy")
    print("2. Play it easy")
    print("3. Play it casual")
    print("4. Play it hard")
    print("5. Play it super hard")
    print("6. Play it god-like")
    print("7. Play it Kratos-like")
    print("")
    print("0. Exit")
    print("")

    while True:
        user_choice = input("Make your selection: ")

        try:
            if user_choice in ("1", "2", "3", "4", "5", "6", "7"):
                os.system("clear")
                hanoi_game(user_choice)
                return 0

            elif user_choice in ("n", "N", "0", "non", "Non", "non", "Non", "exit", "Exit"):
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


def translate_difficulty_level(user_input):

    return {"1": 2,
            "2": 3,
            "3": 5,
            "4": 6,
            "5": 8,
            "6": 10,
            "7": 15}[user_input]


def remove_whitespace(user_input):

    while " " in user_input:
        user_input = user_input.replace(" ", "")

    return user_input


def hanoi_game(difficulty_level):

    towers_size = translate_difficulty_level(difficulty_level)

    tower1 = hanoi_solver.create_hanoi_tower(towers_size)
    tower2 = towers_manipulation.create_no_ring_hanoi_tower(towers_size)
    tower3 = towers_manipulation.create_no_ring_hanoi_tower(towers_size)
    towers = [tower1, tower2, tower3]
    solution = [] + tower1

    os.system("clear")
    print("\n")
    hanoi_ascii.print_towers(towers)
    print("\n")

    while True:

        if towers[1] == solution:
            print("\n==========================================================")
            print("============ Congratulations! You won :D !  ==============")
            print("==========================================================")

            while True:
                try:
                    go_on = input("\nDo you want to go back to main menu? ")

                    if go_on in ("y", "Y", "o", "O", "yes", "Yes", "oui", "Oui"):
                        os.system("clear")
                        return 0

                    elif go_on in ("n", "N", "no", "No", "non", "Non"):
                        sys.exit(0)

                    else:
                        raise ValueError

                except ValueError:
                    pass

        user_input = input("Enter your movement: ")

        try:
            if not user_input:
                raise ValueError

            elif user_input in ("q", "Q", "l", "L", "quit",
                                "Quit", "exit", "Exit", "leave", "Leave"):
                sys.exit(0)

            user_input = remove_whitespace(user_input)
            res_list = [user_input[0], translate_tower_index(user_input[1])]

            if int(res_list[0]) in range(1, towers_size+1) and res_list[1] in (1, 2, 3):
                towers = towers_manipulation.move_ring(res_list, towers)
                os.system("clear")
                hanoi_ascii.print_towers(towers)
                print("\n")

            else:
                raise ValueError

        except ValueError:
            print("Invalid movement!")


def main():

    while True:
        print("")
        main_title()
        print("\n")
        main_menu()
        print("\n")


main()
