#!/usr/bin/env python3

import sys
import hanoi_solver
import hanoi_ascii
import towers_manipulation


import curses
from curses import wrapper
from curses import napms


def main_title(stdscr):
    stdscr.addstr("__/\\\\\\________/\\\\\\__________________________________________________        \n")
    napms(100)
    stdscr.refresh()
    stdscr.addstr(" _\\/\\\\\\_______\\/\\\\\\__________________________________________________       \n")
    napms(100)
    stdscr.refresh()
    stdscr.addstr("  _\\/\\\\\\_______\\/\\\\\\_____________________________________________/\\\\\\_      \n")
    napms(100)
    stdscr.refresh()
    stdscr.addstr("   _\\/\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\__/\\\\\\\\\\\\\\\\\\_____/\\\\/\\\\\\\\\\\\_______/\\\\\\\\\\____\\///__     \n")
    napms(100)
    stdscr.refresh()
    stdscr.addstr("    _\\/\\\\\\/////////\\\\\\_\\////////\\\\\\___\\/\\\\\\////\\\\\\____/\\\\\\///\\\\\\___/\\\\\\_    \n")
    napms(100)
    stdscr.refresh()
    stdscr.addstr("     _\\/\\\\\\_______\/\\\\\\___/\\\\\\\\\\\\\\\\\\\\__\\/\\\\\\__\\//\\\\\\__/\\\\\\__\//\\\\\\_\\/\\\\\\_   \n")
    napms(100)
    stdscr.refresh()
    stdscr.addstr("      _\\/\\\\\\_______\\/\\\\\\__/\\\\\\/////\\\\\\__\\/\\\\\\___\\/\\\\\\_\\//\\\\\\__/\\\\\\__\\/\\\\\\_  \n")
    napms(100)
    stdscr.refresh()
    stdscr.addstr("       _\\/\\\\\\_______\\/\\\\\\_\\//\\\\\\\\\\\\\\\\/\\\\_\\/\\\\\\___\\/\\\\\\__\\///\\\\\\\\\\/___\\/\\\\\\_ \n")
    napms(100)
    stdscr.refresh()
    stdscr.addstr("        _\\///________\\///___\\////////\\//__\\///____\\///_____\\/////_____\\///__\n\n")


def main_menu(stdscr):
    stdscr.addstr("1. Play it super easy\n")
    stdscr.addstr("2. Play it easy\n")
    stdscr.addstr("3. Play it casual\n")
    stdscr.addstr("4. Play it hard\n")
    stdscr.addstr("5. Play it super hard\n")
    stdscr.addstr("6. Play it god-like\n")
    stdscr.addstr("7. Play it Kratos-like\n")
    stdscr.addstr("\n")
    stdscr.addstr("0. Exit\n")
    stdscr.addstr("\n")

    while True:
        stdscr.addstr("Make your selection: ")
        user_choice = stdscr.getkey()

        try:
            if user_choice in ("1", "2", "3", "4", "5", "6", "7"):
                stdscr.clear()
                hanoi_game(stdscr, user_choice)
                return 0

            elif user_choice in ("n", "N", "0", "non", "Non", "non", "Non", "exit", "Exit"):
                stdscr.clear()
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


def endgame_menu(scr, towers, difficulty_level, moves_counter):

    towers_size = translate_difficulty_level(difficulty_level)
    expected_moves = 2**towers_size - 1

    scr.addstr("\n\n==========================================================")
    scr.addstr("\n============ Congratulations! You won :D !  ==============")
    scr.addstr("\n==========================================================\n\n")

    scr.addstr("You made "
               + str(moves_counter)
               + " moves out of the "
               + str(expected_moves)
               + " minimum move! \n")

    while True:
        try:
            scr.addstr("\nDo you want to play solution? ")
            go_on = scr.getkey()

            if go_on in ("y", "Y", "o", "O", "yes", "Yes", "oui", "Oui"):
                animation_speed = hanoi_solver.solution_animation_speed(difficulty_level)
                scr.clear()
                hanoi_solver.play_solution(scr, towers_size, animation_speed)
                break

            elif go_on in ("n", "N", "no", "No", "non", "Non"):
                break

            else:
                raise ValueError

        except ValueError:
            pass

    while True:
        try:
            scr.addstr("\nDo you want to go back to main menu? ")
            go_on = scr.getkey()

            if go_on in ("y", "Y", "o", "O", "yes", "Yes", "oui", "Oui"):
                scr.clear()
                return 0

            elif go_on in ("n", "N", "no", "No", "non", "Non"):
                scr.clear()
                sys.exit(0)

            else:
                raise ValueError

        except ValueError:
            pass


def hanoi_game(stdscr, difficulty_level):

    towers_size = translate_difficulty_level(difficulty_level)

    tower1 = hanoi_solver.create_hanoi_tower(towers_size)
    tower2 = towers_manipulation.create_no_ring_hanoi_tower(towers_size)
    tower3 = towers_manipulation.create_no_ring_hanoi_tower(towers_size)
    towers = [tower1, tower2, tower3]
    win_condition = [] + tower1
    moves_counter = 0

    stdscr.clear()
    stdscr.addstr("\n\n")
    hanoi_ascii.print_towers(stdscr, towers)
    stdscr.addstr("\n")

    while True:

        if towers[1] == win_condition:
            return endgame_menu(stdscr, towers, difficulty_level, moves_counter)

        stdscr.addstr("\n")
        stdscr.addstr("Enter your movement: ")
        curses.echo()
        user_input = stdscr.getkey()

        try:
            if user_input in ("q", "Q", "l", "L", "quit",
                                "Quit", "exit", "Exit", "leave", "Leave"):
                stdscr.clear()
                sys.exit(0)

            elif user_input in ("b", "B", "back", "Back", "r", "R", "return"):
                stdscr.clear()
                return 0

            elif user_input == "s":
                animation_speed = hanoi_solver.solution_animation_speed(difficulty_level)
                hanoi_solver.play_solution(stdscr, towers_size, animation_speed)
                stdscr.clear()
                stdscr.addstr("\n\n")
                hanoi_ascii.print_towers(stdscr, towers)
                stdscr.addstr("\n")
                continue

            targeted_tower = stdscr.getkey()
            curses.noecho()
            res_list = [user_input, towers_manipulation.translate_tower_index(targeted_tower)]

            if int(res_list[0]) in range(1, towers_size+1) and res_list[1] in (1, 2, 3):
                moves_counter += 1
                towers = towers_manipulation.move_ring(res_list, towers)
                stdscr.clear()
                stdscr.addstr("\n\n")
                hanoi_ascii.print_towers(stdscr, towers)
                stdscr.addstr("\n")

            else:
                raise ValueError

        except ValueError:
            stdscr.addstr("\nInvalid movement!")


def main(stdscr):

    stdscr.clear()
    while True:
        stdscr.clear()
        stdscr.addstr("\n")
        main_title(stdscr)
        stdscr.addstr("\n\n")
        main_menu(stdscr)
        stdscr.addstr("\n\n")


wrapper(main)
