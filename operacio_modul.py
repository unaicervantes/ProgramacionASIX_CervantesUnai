#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
"""
operacio_modul.py
exercici per a aprendre a utilitzar excepcions.
"""

__author__ = "Unai Cervantes"

def main(dividend, divisor):
    """
    >>> main(20, 5)
    0
    >>> main(22, 5)
    2
    >>> main(20, 0)
    'Paràmetre invàlid, no és possible realitzar la operació.'
    """
    try:
        return dividend % divisor
    except ZeroDivisionError:
        print("'Paràmetre invàlid, no és possible realitzar la operació.'")


if __name__ == "__main__":
    print(main(int(sys.argv[1]), int(sys.argv[2])))