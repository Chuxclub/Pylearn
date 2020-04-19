#!/usr/bin/env python3


def create_hidden_word(word):

    hidden_word = ""

    for i in range(0, len(str(word)) - 1):
        hidden_word = hidden_word + "*"

    return hidden_word


def search_letter(user_letter, hidden_word):

    pos_list = []
    hidden_word_end = len(hidden_word)
    i = 0

    while i < hidden_word_end:

        if user_letter == hidden_word[i]:
            pos_list.append(i)

        i += 1

    return pos_list


def reveal_letters(pos_list, user_letter, hidden_word):

    s = list(hidden_word)

    for i in range(0, len(pos_list)):
        s[pos_list[i]] = user_letter

    return s


# print(reveal_letters(search_letter("e", "test"), "e", create_hidden_word("test")))
# print(reveal_letters(search_letter("t", "test"), "t", create_hidden_word("test")))
# print(reveal_letters(search_letter("a", "test"), "a", create_hidden_word("test")))


# print("".join(str(search_letter("e", "test"))))
# print("".join(str(search_letter("t", "test"))))
# print("".join(str(search_letter("a", "test"))))
