#!/usr/bin/env python3

import word_manipulations
import get_random_word
import hangman_ascii
import sys


def print_ends(hangman_end, guess_word):

    if hangman_end == "defeat":
        print("You lost! Hangman is now dead...")
        print("Guess word was: " + "".join(guess_word))

    else:
        print("You won! Hangman survived thanks to you!")


def is_hidden_word_revealed(hidden_word):
    is_it_revealed = True

    for i in range(0, len(hidden_word)):

        if hidden_word[i] == "*":
            is_it_revealed = False

    return is_it_revealed


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
    print(rand_word)
    hidden_word = word_manipulations.create_hidden_word(rand_word)

    while not end_of_game:

        user_letter = input("Entrez une lettre: ")
        pos_list = word_manipulations.search_letter(user_letter, rand_word)

        if len(pos_list) != 0:
            hidden_word = word_manipulations.reveal_letters(pos_list, user_letter, hidden_word)
            print("".join(hidden_word))

        else:
            hangman_state += 1
            hangman_ascii.hangman_states(hangman_state)
            print("".join(hidden_word))

        end_of_game = is_it_the_end(hangman_state, hidden_word, rand_word)

    while True:
        try:
            keep_playing = input("Do you want to keep playing? ")

            if keep_playing == 'y':
                hangman()

            elif keep_playing == 'n':
                sys.exit(0)

            else:
                raise ValueError("Input must be either 'y' or 'n'")

        except ValueError:
            pass
        
        
