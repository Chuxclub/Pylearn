#!/usr/bin/env python3


# Function to print a line in the center of screen


def print_menu(scr, menu):

    h, w = scr.getmaxyx()

    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx

        scr.addstr(y, x, row)

    scr.refresh()
