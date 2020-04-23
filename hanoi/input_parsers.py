#!/usr/bin/env python3


# Author: Florian Legendre
#
# What: Simple switch/case-like function returning a tower_size as an int
#
# How : It uses a dictionary with a key corresponding to the passed parameter
#
# Why: \
#
# Complexity (time): O(1)
#
# Self-Criticism: \

def translate_difficulty_level(user_input):

    return {"1": 2,
            "2": 3,
            "3": 5,
            "4": 6,
            "5": 8,
            "6": 10,
            "7": 15}[user_input]


# Author: Florian Legendre
#
# What: Checks all occurences of a single whitespace and removes it.   
#
# How : If there are several contiguous whitespaces it works too as
#       a contiguous whitespace is still a series of individual whitespaces...
#
#       Removal is made by replacing the whitespaces with an empty string
#
# Why: \
#
# Complexity (time): O(len(user_input)) => linear.
#
# Self-Criticism: Perhaps there's better than a linear complexity

def remove_whitespace(user_input):

    while " " in user_input:
        user_input = user_input.replace(" ", "")

    return user_input


# Author: Florian Legendre
#
# What: These two functions just check lengthy conditions
#
# How : \
#
# Why: Readibility candies so to speak
#
# Complexity (time): O(1) as the condition is constant...
#
# Self-Criticism: \

def is_int(user_input):

    return user_input in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")


def is_tower_id(user_input):

    return user_input in ("a", "A", "b", "B", "c", "D")


# Author: Florian Legendre
#
# What: Receives a possibly valid string (> 2) and returns a list
#       containing a ring_id and a tower_id both as strings.
#
# How : First for loop checks if it detects a number (is_int() doesn't
#       detects if there's an int but if there's a number as a string).
#       Lengthy number strings aren't authorized. As the hanoi tower problem
#       solutions as complexity of O(tower_size²-1) 2^99 - 1 is such a big
#       number that I don't authorize more than digits ring ids. This explains
#       the count < 2 condition.
#
#       Second for loop simply collects any "a","b","c" character it finds. If the
#       targeted_tower_id ends up being wrong it will be detected in hanoi_game() loop.
#       If a long string of "a","b","c"s is entered a -1, -1 will be caught by the
#       hanoi_game() loop.
#
#       So we basically end up with three scenarios: 3 characters list, a 2 characters list
#       and any other invalid case. A 3 character list corresponds, for example, to 10c.
#       A two character list to 1c.
#
#       As the first for loops looks for numbers and the second one for "a","b","c"s,
#       an input such as b1 is allowed to as it will end up being sorted 1b in the returned
#       res list.
#
#       Even if there's a 3 characters list or 2 characters list, invalid inputs will be detected
#       in the hanoi_game loop() right after the input_parse() call.
#
# Why: \
#
# Complexity (time): O(2*len(user_input))
#
# Self-Criticism: Running twice through the user_input implies a serious threat on the program
#                 stability in case of a very long string.

def input_parse(user_input):

    str_to_parse = remove_whitespace(user_input)
    len_str = len(str_to_parse)
    temp_res = []
    count = 0

    for i in range(len_str):

        if is_int(str_to_parse[i]) and count < 2:
            temp_res.append(str_to_parse[i])
            count += 1

    for i in range(len_str):
        if is_tower_id(str_to_parse[i]):
            temp_res.append(str_to_parse[i])

    res = []

    if len(temp_res) == 3:
        ring_id = "".join(str(temp_res[0]) + str(temp_res[1]))
        tower_id = "".join(str(temp_res[2]))
        res.append(ring_id)
        res.append(tower_id)

    elif len(temp_res) == 2:
        ring_id = "".join(str(temp_res[0]))
        tower_id = "".join(str(temp_res[1]))
        res.append(ring_id)
        res.append(tower_id)

    else:
        res.append("-1")
        res.append("-1")

    return res
