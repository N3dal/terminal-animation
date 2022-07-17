#!/usr/bin/python3
# -----------------------------------------------------------------
# this is one of my 50 python projects challenge.
#
# simple try to make animation module.
#
# Author:N84.
#
# Create Date:Thu Jun 16 07:58:41 2022.
# ///
# ///
# ///
# -----------------------------------------------------------------
# TO-DO:
# 1) add loading bar with # and when the # collide with [],
# change to * and return it to # collide effect.

# 2)add loading bar like windows bar:
# [      #######              ]
# and will continue forward and start from start:
# [                      #####]
# [             ########      ]
# [###                       #]
# [#####                      ]
# 3) add function that run any loading screen you have write,
# in this file randomly.
# 4) add loading bar go reverse if it reach the end:
# [          ->          ]
# [                    ->]
# [                    <-]
# [          <-          ]
# and rebeat the cycle.
# 5) add loading bar look like this:
# [         <-->         ]
# the <--> move to the right and left for-ever.
# 6) add more loading bars, any ideas?.

from time import sleep as delay
from os import name as OS_NAME
from os import system


def clear():
    """wipe terminal screen."""

    if OS_NAME == "posix":
        # for *nix machines.
        system("clear")

    else:
        # for windows machines.
        system("cls")


def loading_bar1(main_char: str = "#", char_range: int = 50, delay_time: float = 1e-1):
    """show to us a normal loading bar that use any char as indicator."""

    # guard conditions.

    # first make sure that we only use one char not a whole string.
    fill_char = main_char[0]

    # first create empty bar.
    loading_bar = "[" + (" " * char_range) + "]"

    # now convert that loading_bar to list.
    loading_bar = list(loading_bar)

    for index, char in enumerate(loading_bar, 0):
        # clear()
        if char in "[]":
            continue
        loading_bar[index] = fill_char
        print(f"\r{''.join(loading_bar)}", end='')
        delay(delay_time)

    # return indicator for tell that the operation is done.
    return True


def loading_bar2(main_chars: str = "#=>", char_range: int = 50, delay_time: float = 1e-1):
    """show updated bar of the loading_bar1 this uses more than one char to draw the bar."""

    fill_char, moving_char = main_chars[0], main_chars[-1]

    loading_bar = "[" + (fill_char * char_range) + "]"

    # now convert that to list.
    loading_bar = list(loading_bar)

    for index, char in enumerate(loading_bar, 0):
        # clear()
        if char in "[]":
            continue
        loading_bar[index] = moving_char
        print(f"\r{''.join(loading_bar)}", end='')
        delay(delay_time)

    return True


def loading_bar4(main_chars: str = "#", char_range: int = 50, delay_time: float = 1e-1):
    """loading bar like windows bar:
    # [      #######              ]
    # and will continue forward and start from start:
    # [                      #####]
    # [             ########      ]
    # [###                       #]
    # [#####                      ]
    """

    # create an empty bar.
    loading_bar = "[" + (" "*char_range) + "]"

    # convert loading bar to list.
    loading_bar = list(loading_bar)


def loading_words(main_word: str = "loading", iteration: int = 5, delay_time: float = 1e-1):
    """show a word that changes it case in sequence order."""

    for _ in range(iteration):

        # convert main_word from string to list.
        main_word_list = list(main_word)

        for index, char in enumerate(main_word_list):
            main_word_list[index] = char.upper()

            if index != 0:
                # make sure to don't use lower when the index is,
                # zero so we don't want to lower the last char if we,
                # on the first index.
                main_word_list[index-1] = main_word_list[index-1].lower()

            print("".join(main_word_list), end='\r')
            delay(delay_time)


def loading_percent(delay_time: float = 1e-1):
    """show loading percentage for users."""

    for percent in range(1, 101):
        percent = f"{percent}".zfill(2) + "%"
        print(percent, end='\r')
        delay(delay_time)


def spinning_slash(delay_time: float = 1e-1, iteration: int = 25, slash_count: int = 1,
                   space: bool = False):
    """print a spinning slash for users while loading something."""

    space = " " if space else ""

    for _ in range(iteration):

        for char in "|/-\\":
            print(f"\r{(char+space)*slash_count}", end="")
            delay(delay_time)

    clear()


def main():
    # loading_words(main_word="Hello", delay_time=0.3)
    # spinning_slash()
    loading_bar2(main_chars="01")


if __name__ == "__main__":
    main()
