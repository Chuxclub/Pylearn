#!/usr/bin/env python3


import hanoi_solver


def create_ring(ind, size):

    if size == 0:
        res = [" "]
        res.append(" " * 2*ind)
        res.append(" ")
        return res

    else:
        res = ["<"]

        for i in range(0, 2*size):
            res.append("-")

        res.append(">")

        return res


def print_tower(tower):

    last_ring = len(tower)

    for i in range(0, last_ring):
        print(" " * (last_ring - i) + "".join(create_ring(tower[i])))


# All towers must have the same size for this function to work
# Which means that if there's no ring: 0 is chosen

def print_towers(towers):

    nb_towers = len(towers)
    last_ring = len(towers[0])

    for j in range(0, last_ring):

        print("")

        for i in range(0, nb_towers):
            print(" " * (last_ring - j)
                  + "".join(create_ring(j+1, towers[i][j]))
                  + " " * (last_ring - j), end="")
