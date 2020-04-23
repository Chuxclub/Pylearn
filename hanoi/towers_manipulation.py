#!/usr/bin/env python3


# Author: Florian Legendre
#
# What: Creates a list with as many 0s as the desired towers size.
#       This list is then returned.
#
# How : \
#
# Why: 0s in the print functions will bring up only whitespaces as
#      it means there's no ring.
#
# Complexity (time): O(size) => linear
#
# Self-Criticism: \

def create_no_ring_hanoi_tower(size):

    res_tower = []

    for i in range(size):
        res_tower.append(0)

    return res_tower


# Author: Florian Legendre
#
# What: Searches a ring identified by its id (an int) in the towers
#       lists structures. It returns a list containing the id of the tower
#       where the ring is located, its place in this tower (j variable) for
#       the print_towers function and the ring id.
#
# How : A simple while/exception loop detects if the ring id is valid or not.
#       Actually it's a relic and is never used because of the input parser 
#       (input_parsers module) I've added later. I leave it alone just in case...
#
# Why: \
#
# Complexity (time): The number of towers is a constant. So O(3*towers_size)
#
# Self-Criticism: \

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


# Author: Florian Legendre
#
# What: A given ring must be inserted right above a below ring and
#       not two lines aboves. That's basically what this function does.
#
# How : I start the search at the maximum index and then decrements to 0.
#       Indeed, the maximum index corresponds to the BOTTOM of the tower
#       while the 0 to its TOP.
#
# Why: This choice (BOTTOM/TOP) ensured betters complexities and hence faster
#      executions.
#
# Complexity (time): O(tower_size). It's a given tower as indicated in the function
#                    parameter so no need to go through the three towers.
#
# Self-Criticism: \

def search_place_to_insert(tower):

    res = -1

    for i in range(len(tower)-1, -1, -1):

        if tower[i] == 0:
            return i

    return res


# Author: Florian Legendre
#
# What: Moves a ring from one line on a given tower to another
#       tower on the first available place. This function is a
#       raw_move as it doesn't check movement validity.
#
# How : The ring is moved on the first place available in order to
#       ensure that no ring will be overwritten. Movement is made thanks
#       to a simple remove/insert in the corresponding data structures (lists)
#
#       user_input_tuple is always the id of the ring followed by the id of the tower.
#       E.g (1, 3) means ring 1 to tower 3
#
# Why: \
#
# Complexity (time): O(tower_size) because of the search_place_to_insert() 
#
# Self-Criticism: raw_move_ring() and move_ring() declares the same local variables
#                 and worse... They independently call search_place_to_insert() which has
#                 a linear complexity. The variable depending on this function called easily
#                 be passed as an argument from move_ring() to raw_move_ring()


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


# Author: Florian Legendre
#
# What: Checks the movement validity (ring under another ring, bigger ring
#       on a smaller ring is forbidden, etc.) and makes the appropriate operations
#       on the data structures (lists)
#
# How : if/elif/else control structures. Returns the towers without any modification
#       if the movement is not valid. Movement is done by raw_move_ring() if valid.
#
# Why: Divide and conquer as always
#
# Complexity (time): O(2*tower_size) in case of a valid movement thanks to bad design
#
# Self-Criticism: Bad design?

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

    elif src_tower == targeted_tower:
        return towers

    else:
        user_input_tuple = [ring_to_move, targeted_tower]
        return raw_move_ring(user_input_tuple, towers)


# Author: Florian Legendre
#
# What: Switch/case like function to return tower_ids based on user_input
#       strings.
#
# How : \
#
# Why: \
#
# Complexity (time): O(1)
#
# Self-Criticism: \

def translate_tower_index(user_input):

    try:

        return {"A": 1,
                "a": 1,
                "1": 1,
                "B": 2,
                "b": 2,
                "2": 2,
                "C": 3,
                "c": 3,
                "3": 3}[user_input]

    except KeyError:
        pass
