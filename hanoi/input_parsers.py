#!/usr/bin/env python3


def translate_difficulty_level(user_input):

    return {"1": 2,
            "2": 3,
            "3": 5,
            "4": 6,
            "5": 8,
            "6": 10,
            "7": 15}[user_input]


def remove_whitespace(user_input):

    while " " in user_input:
        user_input = user_input.replace(" ", "")

    return user_input


def is_int(user_input):

    return user_input in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")


def is_tower_id(user_input):

    return user_input in ("a", "A", "b", "B", "c", "D")


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
