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


def main():
    pass


if __name__ == "__main__":
    main()
