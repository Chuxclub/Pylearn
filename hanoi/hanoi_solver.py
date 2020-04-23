#!/usr/bin/env python3

import towers_manipulation
import os
import hanoi_ascii
import time


# Author: Florian Legendre
#
# What: Returns a list with ints [1, 2, 3, ...] as long as the
#       desired size of the towers (tower_size argument)
#
# How : \
#
# Why: \
#
# Complexity (time): O(tower_size)
#
# Self-Criticism: \

def create_hanoi_tower(tower_size):

    res_tower = []

    for i in range(1, tower_size + 1):
        res_tower.append(i)

    return res_tower


# Author: Florian Legendre
#
# What: Returns a list of all the movements to do in order to win the game.
#       List items are formatted as follow (ring_id, tower_src, target_tower)
#
#
# How : As only rings on tops of the towers can be moved, ring_id = tower[0]
#       A single tower is passed in the function argument as we want to move
#       a single tower from one place to an empty other place...
#
# Why: solution parameter is an accumulator saving along the recursivity allowed
#      the moves necessary. As this accumulator always starts empty ([]...) it's
#      unnecessary to call the solver with this parameter. This why there's a
#      hanoi_solver() function which merely calls this critical function with
#      the empty list.
#
# Complexity (time): O(2^towers_size - 1)
#
# Self-Criticism: \

def hanoi_solver_aux(tower, dep, arr, mid, solution):

    tower_size = len(tower)

    if tower_size == 1:
        solution.append((tower[0], dep, arr))

    else:
        last_ring = len(tower) - 1
        new_tower = tower[:last_ring]
        temp_solution = hanoi_solver_aux(new_tower, dep, mid, arr, solution)
        temp_solution.append((tower[last_ring], dep, arr))
        solution = hanoi_solver_aux(new_tower, mid, arr, dep, temp_solution)

    return solution


def hanoi_solver(tower_size):

    return hanoi_solver_aux(create_hanoi_tower(tower_size), "A", "B", "C", [])


# Author: Florian Legendre
#
# What: Prints the lists of the solution given by hanoi_solver() on screen
#
# How : \
#
# Why: Used for debugging not for the game in itself
#
# Complexity (time): O(2^towers_size - 1)
#
# Self-Criticism: \

def print_solution(solution_list):

    list_max_index = len(solution_list)

    for i in range(0, list_max_index):
        print(solution_list[i])


# Author: Florian Legendre
#
# What: \
#
# How : \
#
# Why: \
#
# Complexity (time): \
#
# Self-Criticism: \

def solution_animation_speed(difficulty_level):

    return {"1": 1,
            "2": 1,
            "3": 1,
            "4": 0.3,
            "5": 0.1,
            "6": 0.05,
            "7": 0.01}[difficulty_level]


# Author: Florian Legendre
#
# What: Plays the cinematic of the solution
#
# How : It simply follows the solution recipe given by the hanoi_solver
#       by feeding its items one after the other to the move_ring() and
#       print_towers() functions in towers_manipulation and hanoi_ascii
#       modules
#
#       After each print, the screen is cleared and a new print begins.
#       This is what actually gives the impression of an animation. (This
#       is actually the basis of animation itself)
#
# Why: For fun and it because it looks sick
#
# Complexity (time): O(2^towers_size - 1)
#
# Self-Criticism: \

def play_solution(towers_size, speed):

    tower1 = create_hanoi_tower(towers_size)
    tower2 = towers_manipulation.create_no_ring_hanoi_tower(towers_size)
    tower3 = towers_manipulation.create_no_ring_hanoi_tower(towers_size)
    towers = [tower1, tower2, tower3]

    solution_length = 2**towers_size - 1
    solution_recipe = hanoi_solver(towers_size)

    os.system("clear")
    print("\n")
    hanoi_ascii.print_towers(towers)
    print("")
    time.sleep(speed)
    os.system("clear")

    for i in range(solution_length):

        if i == solution_length - 1:
            targeted_tower = towers_manipulation.translate_tower_index(solution_recipe[i][2])
            ring_move = [solution_recipe[i][0], targeted_tower]
            towers_manipulation.move_ring(ring_move, towers)
            print("\n")
            hanoi_ascii.print_towers(towers)
            print("")
            time.sleep(2)
            os.system("clear")

        else:
            targeted_tower = towers_manipulation.translate_tower_index(solution_recipe[i][2])
            ring_move = [solution_recipe[i][0], targeted_tower]
            towers_manipulation.move_ring(ring_move, towers)
            print("\n")
            hanoi_ascii.print_towers(towers)
            print("")
            time.sleep(speed)
            os.system("clear")
