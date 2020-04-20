#!/usr/bin/env python3

import hanoi_solver
import hanoi_ascii


def search_ring(ring_id, towers):

    nb_towers = len(towers)
    towers_height = len(towers[0])
    chosen_ring = ring_id

    while True:
        try:
            if chosen_ring < 0 or chosen_ring > towers_height:
                raise ValueError("Ring doesn't exist")

            else:
                for i in range(0, nb_towers):

                    for j in range(0, towers_height):

                        if towers[i][j] == ring_id:
                            return i

        except ValueError:
            chosen_ring = input("Provided ring id is wrong, please enter a valid ring id: ")


def search_place_to_insert(tower):

    res = -1

    for i in tower:

        if tower[i] == 0:
            res = (i + len(tower) - 1) % len(tower)

    assert res >= 0

    return res


# user_input_tuple is always the id of the ring
# followed by the id of the tower. E.g (1, 3) means
# ring 1 to tower 3

def move_ring(user_input_tuple, towers):

    ring_to_move = int(user_input_tuple[0])
    targeted_tower = int(user_input_tuple[1]) - 1
    src_tower = int(search_ring(ring_to_move, towers))
    new_place = search_place_to_insert(towers[targeted_tower])

    towers[targeted_tower].remove(towers[targeted_tower][0])
    towers[targeted_tower].insert(new_place, ring_to_move)
    towers[src_tower].remove(ring_to_move)
    towers[src_tower].insert(0, 0)

    return towers


# tower1 = hanoi_solver.create_hanoi_tower(5)
# tower2 = [0, 0, 0, 0, 0]
# tower3 = [0, 0, 0, 0, 0]

# towers = [tower1, tower2, tower3]
# hanoi_ascii.print_towers(towers)
# print("")

# towers = move_ring(("1", "3"), towers)
# hanoi_ascii.print_towers([tower1, tower2, tower3])
# print("")
