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


def loading_bar1(main_char: str = "#", char_range: int = 50, delay_time: float = 0.3):
    """show to us a normal loading bar that use char as indicator."""

    # guard conditions.

    # first make sure that we only use one char not a whole string.
    main_char = main_char[0]

    # first create empty bar.
    loading_bar = "[" + (" " * char_range) + "]"

    # now convert that loading_bar to list.
    loading_bar = list(loading_bar)

    for index, _ in enumerate(loading_bar, 1):
        loading_bar[index] = main_char
        print("".join(loading_bar), end='\r')
        delay(delay_time)

    # return indicator for tell that the operation is done.
    return True


def main():
    loading_bar1()


if __name__ == "__main__":
    main()