#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import sys, os

"""
taula_de_multiplicar.py rep un nombre com a paràmetre i imprimeix la seva taula de multiplicar.
"""
__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"

def main(nombre_protagonista):
    """
    rep un nombre com a paràmetre i retorna la seva taula de multiplicar en forma de cadena de text.
    >>> print(main(5))
    5 x 1 = 5
    5 x 2 = 10
    5 x 3 = 15
    5 x 4 = 20
    5 x 5 = 25
    5 x 6 = 30
    5 x 7 = 35
    5 x 8 = 40
    5 x 9 = 45
    5 x 10 = 50
    <BLANKLINE>
    >>> print(main(-3))
    -3 x 1 = -3
    -3 x 2 = -6
    -3 x 3 = -9
    -3 x 4 = -12
    -3 x 5 = -15
    -3 x 6 = -18
    -3 x 7 = -21
    -3 x 8 = -24
    -3 x 9 = -27
    -3 x 10 = -30
    <BLANKLINE>
    """
    taula_result = ""
    for multiplicador in range(1,11):
        taula_result += f"{nombre_protagonista} x {multiplicador} = {nombre_protagonista * multiplicador}\n"
    return taula_result

if __name__ == "__main__":
    try:
        print(main( \
            int( \
                sys.argv[1] \
            ) \
        ))
    except:
        print("Mode d'ús:")
        print("python3 taula_de_multiplicar.py <nombre_sencer>")