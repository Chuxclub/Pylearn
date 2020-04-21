#!/usr/bin/env python3


import hanoi_solver


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


def print_towers(towers):

    nb_towers = len(towers)
    max_ring = len(towers[0])
    res_ring_line = []

    for j in range(0, max_ring):

        for i in range(0, nb_towers):

            res_ring_line.extend(create_ring(towers[i][j], max_ring))
            res_ring_line.append(" ")

        print("".join(res_ring_line))
        res_ring_line = []

    print("".join(print_floor(max_ring)))
