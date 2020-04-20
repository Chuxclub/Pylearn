#!/usr/bin/env python3


def hangman_state1():
    print("============ ")


def hangman_state2():
    print("   |         ")
    print("   |         ")
    print("   |         ")
    print("============ ")


def hangman_state3():
    print("   ________  ")
    print("   |         ")
    print("   |         ")
    print("   |         ")
    print("   |         ")
    print("   |         ")
    print("   |         ")
    print("============ ")


def hangman_state4():
    print("   ________  ")
    print("   |/        ")
    print("   |         ")
    print("   |         ")
    print("   |         ")
    print("   |         ")
    print("   |         ")
    print("============ ")


def hangman_state5():
    print("   ________    ")
    print("   |/     |    ")
    print("   |           ")
    print("   |           ")
    print("   |           ")
    print("   |           ")
    print("   |           ")
    print("============   ")


def hangman_state6():
    print("   ________  ")
    print("   |/     |  ")
    print("   |      o  ")
    print("   |         ")
    print("   |         ")
    print("   |         ")
    print("   |         ")
    print("============ ")


def hangman_state7():
    print("   ________   ")
    print("   |/     |   ")
    print("   |      o   ")
    print("   |     /|\\ ")
    print("   |          ")
    print("   |          ")
    print("   |          ")
    print("============  ")


def hangman_state8():
    print("   ________   ")
    print("   |/     |   ")
    print("   |      o   ")
    print("   |     /|\\ ")
    print("   |     / \\ ")
    print("   |          ")
    print("   |          ")
    print("============  ")


def hangman_states(case):
    switcher = {
        1: hangman_state1,
        2: hangman_state2,
        3: hangman_state3,
        4: hangman_state4,
        5: hangman_state5,
        6: hangman_state6,
        7: hangman_state7,
        8: hangman_state8
    }

    return switcher.get(case, "State doesn't exist")()


def hangman_saved():
    print("\\o/")
    print(" | ")
    print("/ \\")
