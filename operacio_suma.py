#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
"""
operacio_suma.py
exercici per a aprendre a utilitzar excepcions.
"""

__author__ = "Unai Cervantes"

def main(sum1, sum2):
    """
    >>> main('20', '5')
    25
    >>> main('22', '5')
    27
    >>> main('20', 'E')
    "invalid literal for int() with base 10: 'E'"
    """
    result = ""
    try:
        result = int(sum1) + int(sum2)
        return result
    except ValueError as e:
        print(f'"{e}"')

if __name__ == "__main__":
    print(main(sys.argv[1], sys.argv[2]))