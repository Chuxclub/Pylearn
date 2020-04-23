#!/usr/bin/env python3


import os


# Author: Florian Legendre
#
# What: Returns a list containing the characters corresponding to a ring.
#       This list will be concatenated with the other rings of the same line
#       in print_towers() below and print as such.
#
# How : In order to always have then same length, whitespaces fill the list
#       corresponding on the size of the ring.
#
#       For example: if ring_size is 0 (size parameter here), then the list only has
#       whitespaces in it. If the ring_size is above 0 then if fills the list with the
#       appropriate characters.
#
#       All the lists (e.g rings) have the same size based on the maximum ring size which
#       also happens to 2 times the size of the towers + 1... For example: my towers have height
#       of 3 lines, then my maximum ring has a size of 7 characters <----->
#
# Why: \
#
# Complexity (time): O(2*tower_size)
#
# Self-Criticism: \

def create_ring(size, max_size):

    res_ring = []
    middle = max_size
    fst_bracket = max_size - size
    lst_bracket = max_size + size

    if size == 0:
        for i in range(2*max_size+1):
            res_ring.append(" ")

    else:

        for i in range(2*max_size+1):

            if i == fst_bracket:
                res_ring.append("<")

            elif i == middle and size > 1:
                res_ring.append(str(size))

            elif i > fst_bracket and i < lst_bracket:
                res_ring.append("-")

            elif i == lst_bracket:
                res_ring.append(">")

            else:
                res_ring.append(" ")

    return res_ring


# Author: Florian Legendre
#
# What: Same idea as above but for the floor ====A====B====C==== below the towers
#
# How : See above
#
# Why: \
#
# Complexity (time): O(2*towers_size)
#
# Self-Criticism: \

# All towers must have the same size for this function to work
# Which means that if there's no ring: 0 is chosen

def print_floor(max_size):

    res_floor = []

    for i in range((2*max_size+1)*3 + 2):

        if i == max_size:
            res_floor.append("A")

        elif i == (2*max_size+1)+1+max_size:
            res_floor.append("B")

        elif i == (2*max_size+1)*2+2+max_size:
            res_floor.append("C")

        else:
            res_floor.append("=")

    return res_floor


# Author: Florian Legendre
#
# What: Concatenates all the lists produced byt the functions above
#       and print the result on the screen line by line thanks to a
#       for loop from top to bottom.
#
# How : The floor is printed out and after the loop as its size is constant and
#       thus being more simple to produce. + It's on the bottom.
#
# Why: \
#
# Complexity (time): O(towers_size²)
#
# Self-Criticism: \

def print_towers(towers):

    w, h = os.get_terminal_size()
    vertical_align = "\n" * int(h/4)
    print(vertical_align)

    nb_towers = len(towers)
    max_ring = len(towers[0])
    res_ring_line = []

    for j in range(0, max_ring):

        for i in range(0, nb_towers):

            res_ring_line.extend(create_ring(towers[i][j], max_ring))
            res_ring_line.append(" ")

        print("".join(res_ring_line).center(w))
        res_ring_line = []

    print("".join(print_floor(max_ring)).center(w))
