#!/usr/bin/env python3


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
    
    for i in range(0, list_max_index) :
        print(solution_list[i])
