#!/usr/bin/env python3

import sys
import hanoi_solver
import hanoi_ascii
import towers_manipulation
import os
import subprocess

from pretty_term import print_menu
from curses import *

def main_title(scr):
    h, w = scr.getmaxyx()

    scr.addstr(3, w//2 - 40, "__/\\\\\\________/\\\\\\__________________________________________________        ")
    napms(100)
    scr.refresh()
    scr.addstr(4, w//2 - 40, " _\\/\\\\\\_______\\/\\\\\\__________________________________________________       ")
    napms(100)
    scr.refresh()
    scr.addstr(5, w//2 - 40, "  _\\/\\\\\\_______\\/\\\\\\_____________________________________________/\\\\\\_      ")
    napms(100)
    scr.refresh()
    scr.addstr(6, w//2 - 40, "   _\\/\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\__/\\\\\\\\\\\\\\\\\\_____/\\\\/\\\\\\\\\\\\_______/\\\\\\\\\\____\\///__     ")
    napms(100)
    scr.refresh()
    scr.addstr(7, w//2 - 40, "    _\\/\\\\\\/////////\\\\\\_\\////////\\\\\\___\\/\\\\\\////\\\\\\____/\\\\\\///\\\\\\___/\\\\\\_    ")
    napms(100)
    scr.refresh()
    scr.addstr(8, w//2 - 40, "     _\\/\\\\\\_______\/\\\\\\___/\\\\\\\\\\\\\\\\\\\\__\\/\\\\\\__\\//\\\\\\__/\\\\\\__\//\\\\\\_\\/\\\\\\_   ")
    napms(100)
    scr.refresh()
    scr.addstr(9, w//2 - 40, "      _\\/\\\\\\_______\\/\\\\\\__/\\\\\\/////\\\\\\__\\/\\\\\\___\\/\\\\\\_\\//\\\\\\__/\\\\\\__\\/\\\\\\_  ")
    napms(100)
    scr.refresh()
    scr.addstr(10, w//2 - 40, "       _\\/\\\\\\_______\\/\\\\\\_\\//\\\\\\\\\\\\\\\\/\\\\_\\/\\\\\\___\\/\\\\\\__\\///\\\\\\\\\\/___\\/\\\\\\_ ")
    napms(100)
    scr.refresh()
    scr.addstr(11, w//2 - 40, "        _\\///________\\///___\\////////\\//__\\///____\\///_____\\/////_____\\///__")


def main_menu(scr):

    h, w = scr.getmaxyx()

    menu = ["Play it super easy", "Play it easy",
            "Play it casual", "Play it hard",
            "Play it super hard", "Play it god-like",
            "Play it Kratos-like"]

    print_menu(scr, menu)

    msg = "0. Exit"
    scr.addstr(int(h/2) - len(menu) + 11, int(w/2) - len(msg), msg)

    while True:
        scr.addstr(int(h/2) - len(menu) + 13, 2, "Make your selection: ")
        user_choice = scr.getkey()

        try:
            if user_choice in ("1", "2", "3", "4", "5", "6", "7"):
                scr.clear()
                hanoi_game(scr, user_choice)
                return 0

            elif user_choice in ("n", "N", "0", "non", "Non",
                                 "non", "Non", "exit", "Exit"):
                scr.clear()
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


def hanoi_game(scr, difficulty_level):

    towers_size = translate_difficulty_level(difficulty_level)

    tower1 = hanoi_solver.create_hanoi_tower(towers_size)
    tower2 = towers_manipulation.create_no_ring_hanoi_tower(towers_size)
    tower3 = towers_manipulation.create_no_ring_hanoi_tower(towers_size)
    towers = [tower1, tower2, tower3]
    win_condition = [] + tower1
    moves_counter = 0

    scr.clear()
    scr.addstr("\n\n")
    hanoi_ascii.print_towers(scr, towers)
    scr.addstr("\n")

    while True:

        if towers[1] == win_condition:
            return endgame_menu(scr, towers, difficulty_level, moves_counter)

        echo()
        nocbreak()

        scr.addstr("\n")
        scr.addstr("Enter ring id: ")
        user_input = scr.getstr().decode(encoding="utf-8")

        noecho()
        cbreak()

        if user_input in ("q", "Q", "l", "L", "quit",
                                "Quit", "exit", "Exit", "leave", "Leave"):
            scr.clear()
            sys.exit(0)

        elif user_input in ("b", "B", "back", "Back", "r", "R", "return"):
            scr.clear()
            return 0

        elif user_input == "s":
            animation_speed = hanoi_solver.solution_animation_speed(difficulty_level)
            hanoi_solver.play_solution(scr, towers_size, animation_speed)
            scr.clear()
            scr.addstr("\n\n")
            hanoi_ascii.print_towers(scr, towers)
            scr.addstr("\n")
            continue

        echo()
        nocbreak()

        scr.addstr("\n")
        scr.addstr("Enter tower id: ")
        targeted_tower = scr.getkey()

        noecho()
        cbreak()

        res_list = [user_input, towers_manipulation.translate_tower_index(targeted_tower)]
        flushinp()

        try:

            if int(res_list[0]) in range(1, towers_size+1) and res_list[1] in (1, 2, 3):
                moves_counter += 1
                towers = towers_manipulation.move_ring(res_list, towers)
                scr.clear()
                scr.addstr("\n\n")
                hanoi_ascii.print_towers(scr, towers)
                scr.addstr("\n")

            else:
                raise ValueError

        except ValueError:
            flushinp()
            scr.addstr("\nInvalid movement!")


def main(scr):

    while True:
        scr.erase()
        scr.border('|', '|', '-', '-', '+', '+', '+', '+')
        main_title(scr)
        main_menu(scr)

subprocess.CREATE_NEW_CONSOLE
wrapper(main)
