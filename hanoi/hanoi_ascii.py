#!/usr/bin/env python3


import hanoi_solver


def create_ring(size):
    res = ["<"]

    for i in range(0, 2*size):
        res.append("-")

    res.append(">")

    return res


def print_tower(tower):

    last_ring = len(tower)

    for i in range(0, last_ring):
        print(" " * (last_ring - i) + "".join(create_ring(tower[i])))

print_tower(hanoi_solver.create_hanoi_tower(5))
