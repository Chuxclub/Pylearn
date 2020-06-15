#!/usr/bin/env python3

import time
import sys
import os
import hanoi_solver
import hanoi_ascii
import towers_manipulation
from input_parsers import *


# Author: Florian Legendre
#
# What: Prints the title of the program on launch with a small animation
#
# How : Animation is made thanks to calls of the sleep function in time library
#
# Why: As the program sleeps regularly the title is slowly revealed giving the "animated"
#      effect. Title is centered thanks to the .center() string method and terminal width
#      variable collected throught get_terminal_size() function in the os library.
#
# Complexity (time): O(1)
#
# Self-Criticism: /

def main_title():
    w, h = os.get_terminal_size()
    print(r"__/\\\________/\\\__________________________________________________        ".center(w))
    time.sleep(0.05)
    print(r" _\/\\\_______\/\\\__________________________________________________       ".center(w))
    time.sleep(0.05)
    print(r"  _\/\\\_______\/\\\_____________________________________________/\\\_      ".center(w))
    time.sleep(0.05)
    print(r"   _\/\\\\\\\\\\\\\\\__/\\\\\\\\\_____/\\/\\\\\\_______/\\\\\____\///__     ".center(w))
    time.sleep(0.05)
    print(r"    _\/\\\/////////\\\_\////////\\\___\/\\\////\\\____/\\\///\\\___/\\\_    ".center(w))
    time.sleep(0.05)
    print(r"     _\/\\\_______\/\\\___/\\\\\\\\\\__\/\\\__\//\\\__/\\\__\//\\\_\/\\\_   ".center(w))
    time.sleep(0.05)
    print(r"      _\/\\\_______\/\\\__/\\\/////\\\__\/\\\___\/\\\_\//\\\__/\\\__\/\\\_  ".center(w))
    time.sleep(0.05)
    print(r"       _\/\\\_______\/\\\_\//\\\\\\\\/\\_\/\\\___\/\\\__\///\\\\\/___\/\\\_ ".center(w))
    time.sleep(0.05)
    print(r"        _\///________\///___\////////\//__\///____\///_____\/////_____\///__".center(w))


# Author: Florian Legendre
#
# What: Brings up the main menu with the prints and while/exception loop
#       for filtering allowed inputs
#
# How : \
#
# Why: Divide and conquer -> here, more readibility thanks to division
#
# Complexity (time): Hard to evaluate if hanoi_game() is played. O(1)
#                    in any other case
#
# Self-Criticism: \

def main_menu():
    w, h = os.get_terminal_size()
    vertical_align = "\n" * int(h/8)
    print(vertical_align)
    print("1. Play it super easy".center(w))
    print("2. Play it easy".center(w))
    print("3. Play it casual".center(w))
    print("4. Play it hard".center(w))
    print("5. Play it super hard".center(w))
    print("6. Play it god-like".center(w))
    print("7. Play it Kratos-like".center(w))
    print("")
    print("0. Exit".center(w))
    print("")

    while True:
        user_choice = input()

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


# Author: Florian Legendre
#
# What: Brings up a menu when the game is over with the possibility
#       to choose between watching the solution to do better next time
#       or going back to the main menu
#
# How : Exceptions allows controlling the undesired inputs, those which
#       don't match the inputs indicated in the previous 'if' conditions
#       statements. Going back to the main menu is made thanks to a 0 returned
#       as this 0 is caught by another return in hanoi_game() hence bringing back
#       the main_menu() where hanoi_game() was initially launched
#
# Why: \
#
# Complexity (time): If the animation is played -> O(n²) as the hanoi_solver has
#                    quadratic complexity
#
# Self-Criticism: The code looks a bit messy. I'm not sure what I could do to improve
#                 readibility

def endgame_menu(towers, difficulty_level, moves_counter):

    towers_size = translate_difficulty_level(difficulty_level)
    expected_moves = 2**towers_size - 1

    w, h = os.get_terminal_size()
    vertical_align = "\n" * int(h/8)
    print(vertical_align)

    print("==========================================================".center(w))
    print("============ Congratulations! You won :D !  ==============".center(w))
    print("==========================================================".center(w))

    print("\n\n")
    print(("You made "
          + str(moves_counter)
          + " moves out of the "
          + str(expected_moves)
          + " minimum move! \n").center(w))

    while True:
        try:
            go_on = input("Do you want to play solution? ".center(w))

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
            os.system("clear")
            print(vertical_align*2)
            go_on = input("Do you want to go back to main menu? ".center(w))

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


# Author: Florian Legendre
#
# What: Brings up the hanoi game loop which is => input > parse input
#       > system applies input > etc. It's basically the core game function
#
# How : Here I say "parse input" because the user can enter any string
#       and the game will analyze this string and make the appropriate
#       operations. Parsing is made in <input_parsers> thanks to
#       input_parse() function.
#
#       Before the input parsing a simple loop
#       checks if an authorized command has been entered which allows
#       leaving the game, playing the solution animation  and such.
#       As moving a ring requires at least two information (ring_id and
#       targeted_tower_id), a first check of an impossible input is done
#       through len(user_input) < 2 condition.
#
#       input_parse() returns a list consisting of a ring_id and a
#       targeted_tower_id which is a string. This last string is converted into
#       an int for the simplicity of the code. If the parser finds an error
#       it returns impossible ids in this game such as -1, -1. 
#
#       Finally, after the input is parsed I check whether or not it corresponds
#       to an existing tower or ring. There are always three towers named 1, 2, 3
#       as ints. An empty tower (no ring) is a tower. So if it catches -1, -1 it
#       immediately acknowledges the error and sends an exception invalidating the movement.
#
#       End of the game is detected thanks to tower2 comparison with initial state of tower1
#       saved in the win_condition variable. Moves_counter simply allows to let the player
#       know in the game menu whether or not they found the optimal solution.
#       Difficulty_level affects the heights of the towers.
#
# Why: \
#
# Complexity (time): Depends on many factors...
#
# Self-Criticism: This way of parsing input is messy or at least could be divided in many
#                 functions

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

        user_input = input()

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

            elif len(user_input) < 2:
                raise ValueError

            user_input = input_parse(user_input)
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


# Author: Florian Legendre
#
# What: Launches the Home menu the game with its title and options
#
# How : Terminal is cleared thanks to the os.system("clear") which
#       simply calls the "clear" in the source terminal in which the
#       program is executed. The rest of this function is fairly self-explanatory.
#
# Why: \
#
# Complexity (time): Depends on many factors...
#
# Self-Criticism: \

def main():

    while True:
        os.system("clear")
        print("")
        main_title()
        print("\n")
        main_menu()
        print("\n")


# ================================== #
# Entry point of the program is here #
# ================================== #

main()
