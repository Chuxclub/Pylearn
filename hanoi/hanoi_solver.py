#!/usr/bin/env python3

import towers_manipulation
import os
import hanoi_ascii
import time


def create_hanoi_tower(tower_size):

    res_tower = []

    for i in range(1, tower_size + 1):
        res_tower.append(i)

    return res_tower


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


def print_solution(solution_list):

    list_max_index = len(solution_list)

    for i in range(0, list_max_index):
        print(solution_list[i])


def solution_animation_speed(difficulty_level):

    return {"1": 1,
            "2": 1,
            "3": 1,
            "4": 0.8,
            "5": 0.5,
            "6": 0.3,
            "7": 0.01}[difficulty_level]


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
        targeted_tower = towers_manipulation.translate_tower_index(solution_recipe[i][2])
        ring_move = [solution_recipe[i][0], targeted_tower]
        towers_manipulation.move_ring(ring_move, towers)
        print("\n")
        hanoi_ascii.print_towers(towers)
        print("")
        time.sleep(speed)
        os.system("clear")
