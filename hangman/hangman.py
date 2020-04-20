#!/usr/bin/env python3

import word_manipulations
import get_random_word
import hangman_ascii
import sys
import os


def print_ends(hangman_end, guess_word):

    if hangman_end == "defeat":
        print("")
        print("You lost! Hangman is now dead...")
        print("Guess word was: " + "".join(guess_word))

    else:
        print("")
        print("You won! Hangman survived thanks to you!")


def is_hidden_word_revealed(hidden_word):
    is_it_revealed = True

    for i in range(0, len(hidden_word)):

        if hidden_word[i] == "*":
            is_it_revealed = False

    return is_it_revealed


# Why string comparison doesn't work here
# with == operator when they are equal???
def is_it_the_end(hangman_state, hidden_word, guess_word):

    if hangman_state == 8:
        print_ends("defeat", guess_word)
        return True

    elif is_hidden_word_revealed(hidden_word):
        print_ends("victory", guess_word)
        return True

    else:
        return False


def hangman():

    hangman_state = 0
    end_of_game = False

    rand_word = get_random_word.get_random_word()
    hidden_word = word_manipulations.create_hidden_word(rand_word)
    user_input_saves = []

    while not end_of_game:
        print("")
        user_letter = input("Entrez une lettre: ")
        print("")
        pos_list = word_manipulations.search_letter(user_letter, rand_word)

        if len(pos_list) != 0:
            hidden_word = word_manipulations.reveal_letters(pos_list, user_letter, hidden_word)
            print("".join(hidden_word))

        else:
            user_input_saves.append(user_letter)
            hangman_state += 1
            os.system("clear")
            hangman_ascii.hangman_states(hangman_state)
            print("")
            print("".join(user_input_saves))
            print("".join(hidden_word))

        end_of_game = is_it_the_end(hangman_state, hidden_word, rand_word)

    while True:
        try:
            keep_playing = input("\nDo you want to keep playing? ")

            if keep_playing in ("1", "o", "O", "y", "Y",
                                "oui", "yes", "Oui", "Yes"):
                os.system("clear")
                hangman()

            elif keep_playing in ("2", "n", "N", "non", "no", "Non", "No"):
                os.system("clear")
                sys.exit(0)

            else:
                raise ValueError("Input must be either 'y' or 'n'")

        except ValueError:
            pass
