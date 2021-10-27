#!/bin/python3
# _*_ coding: utf-8 _*_

"""
   palindrome.py
   avalua si una cadena de text és o no un palindrome
"""
__author__ = "Unai Cervantes"

import sys

def main(text_a_avaluar):
    
    """
    Comprovacions Doctest

    >>> main('A ti bonita')
    No
    >>> main('0.5')
    No
    >>> main('A mama Roma le aviva el amor a papa y a papa Roma le aviva el amor a mama')
    Si
    >>> main('Roma ni se conoce sin oro ni se conoce sin amor')
    Si
    >>> main('1548985885898451')
    Si
    """

    if text_a_avaluar.lower().replace(" ", "") == text_a_avaluar[::-1].lower().replace(" ", ""):
        print("Si")
    else:
        print("No")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Itrodueix una cadena de text per a evaluar si és o no un palíndrome")
        print("Exemple d'ús:")
        print("  $ python3 palindrome.py 'radar'")
        print("  Si")
        quit()

    main(sys.argv[1])
