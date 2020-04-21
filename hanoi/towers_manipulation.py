#!/usr/bin/env python3

# import hanoi_solver
# import hanoi_ascii
# import time


def create_no_ring_hanoi_tower(size):

    res_tower = []

    for i in range(size):
        res_tower.append(0)

    return res_tower


def search_ring(ring_id, towers):

    nb_towers = len(towers)
    towers_height = len(towers[0])
    chosen_ring = ring_id

    while True:

        try:
            if chosen_ring < 1 or chosen_ring > towers_height:
                raise ValueError("Ring doesn't exist")

            else:
                for i in range(nb_towers):

                    for j in range(towers_height):
                        if towers[i][j] == chosen_ring:
                            return [i, j, chosen_ring]

        except ValueError:
            chosen_ring = int(input("Provided ring id is wrong, please enter a valid ring id: "))


def search_place_to_insert(tower):

    res = -1

    for i in range(len(tower)-1, -1, -1):

        if tower[i] == 0:
            return i

    return res


# user_input_tuple is always the id of the ring
# followed by the id of the tower. E.g (1, 3) means
# ring 1 to tower 3

def raw_move_ring(user_input_tuple, towers):

    ring_to_move = int(user_input_tuple[0])
    targeted_tower = int(user_input_tuple[1])
    src_tower = int(search_ring(ring_to_move, towers)[0])
    new_place = search_place_to_insert(towers[targeted_tower])

    towers[targeted_tower].remove(towers[targeted_tower][0])
    towers[targeted_tower].insert(new_place, ring_to_move)
    towers[src_tower].remove(ring_to_move)
    towers[src_tower].insert(0, 0)

    return towers


def move_ring(user_input_tuple, towers):

    ring_to_move = int(user_input_tuple[0])
    summit = 0
    ground = len(towers[0])-1

    src_place = search_ring(ring_to_move, towers)
    src_tower = src_place[0]
    src_line = src_place[1]
    ring_to_move = src_place[2]

    targeted_tower = int(user_input_tuple[1])-1
    targeted_place = search_place_to_insert(towers[targeted_tower])

    if src_line > summit and towers[src_tower][src_line-1] != 0:
        return towers

    elif targeted_place < ground and ring_to_move > towers[targeted_tower][targeted_place+1]:
        return towers

    else:
        user_input_tuple = [ring_to_move, targeted_tower]
        return raw_move_ring(user_input_tuple, towers)
