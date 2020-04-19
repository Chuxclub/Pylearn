#!/usr/bin/env python3


import os
import random

random.seed()


def get_random_word():

    filepath = os.getcwd()
    filename = filepath + '/dictionary.txt'

    with open(filename, 'r') as f:

        random_word = random.randint(0, 41237)
    
        for i in range(0, random_word):
            f.readline()

        chosen_word = f.readline()

    return chosen_word
