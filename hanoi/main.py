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
                os.system("clear")
                sys.exit(0)

            else:
                raise ValueError

        except ValueError:
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


def endgame_menu(towers, difficulty_level, moves_counter):

    towers_size = translate_difficulty_level(difficulty_level)
    expected_moves = 2**towers_size - 1

    print("\n==========================================================")
    print("============ Congratulations! You won :D !  ==============")
    print("==========================================================\n")

    print("You made "
          + str(moves_counter)
          + " moves out of the "
          + str(expected_moves)
          + " minimum move! \n")

    while True:
        try:
            go_on = input("Do you want to play solution? ")

            if go_on in ("y", "Y", "o", "O", "yes", "Yes", "oui", "Oui"):
                animation_speed = hanoi_solver.solution_animation_speed(difficulty_level)
                os.system("clear")
                hanoi_solver.play_solution(towers_size, animation_speed)
                break

            elif go_on in ("n", "N", "no", "No", "non", "Non"):
                break

            else:
                raise ValueError

        except ValueError:
            pass

    while True:
        try:
            go_on = input("\nDo you want to go back to main menu? ")

            if go_on in ("y", "Y", "o", "O", "yes", "Yes", "oui", "Oui"):
                os.system("clear")
                return 0

            elif go_on in ("n", "N", "no", "No", "non", "Non"):
                os.system("clear")
                sys.exit(0)

            else:
                raise ValueError

        except ValueError:
            pass


def hanoi_game(difficulty_level):

    towers_size = translate_difficulty_level(difficulty_level)

    tower1 = hanoi_solver.create_hanoi_tower(towers_size)
    tower2 = towers_manipulation.create_no_ring_hanoi_tower(towers_size)
    tower3 = towers_manipulation.create_no_ring_hanoi_tower(towers_size)
    towers = [tower1, tower2, tower3]
    win_condition = [] + tower1
    moves_counter = 0

    os.system("clear")
    print("\n")
    hanoi_ascii.print_towers(towers)
    print("")

    while True:

        if towers[1] == win_condition:
            return endgame_menu(towers, difficulty_level, moves_counter)

        user_input = input("Enter your movement: ")

        try:
            if user_input in ("q", "Q", "l", "L", "quit",
                                "Quit", "exit", "Exit", "leave", "Leave"):
                os.system("clear")
                sys.exit(0)

            elif user_input in ("b", "B", "back", "Back", "r", "R", "return"):
                os.system("clear")
                return 0

            elif user_input == "s":
                animation_speed = hanoi_solver.solution_animation_speed(difficulty_level)
                hanoi_solver.play_solution(towers_size, animation_speed)
                os.system("clear")
                print("\n")
                hanoi_ascii.print_towers(towers)
                print("")
                continue

            elif len(user_input) != 2:
                raise ValueError

            user_input = remove_whitespace(user_input)
            res_list = [user_input[0], towers_manipulation.translate_tower_index(user_input[1])]

            if int(res_list[0]) in range(1, towers_size+1) and res_list[1] in (1, 2, 3):
                moves_counter += 1
                towers = towers_manipulation.move_ring(res_list, towers)
                os.system("clear")
                print("\n")
                hanoi_ascii.print_towers(towers)
                print("")

            else:
                raise ValueError

        except ValueError:
            print("Invalid movement!")


def main():

    while True:
        os.system("clear")
        print("")
        main_title()
        print("\n")
        main_menu()
        print("\n")


main()
