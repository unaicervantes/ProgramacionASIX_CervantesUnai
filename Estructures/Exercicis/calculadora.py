#!/usr/bin/python3
# _*_ coding: utf-8 _*_

__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"

from multiprocessing.sharedctypes import Value
import sys
from tkinter import E 

def main(numero1,operador,numero2):
    """
    >>> main(4,"+",4)
    8
    >>> main(45,"-",32)
    13
    >>> main(45,"-",46)
    -1
    >>> main(78,"*",98)
    7644
    >>> main(78,"/",3)
    26.0
    >>> main(3,"/",78)
    0.038461538461538464
    >>> main(78,"//",3)
    26
    >>> main(14,"**",54)
    77788236626678808982722471083604074886584214739573349250236416
    >>> main(89,"!",0)
    16507955160908461081216919262453619309839666236496541854913520707833171034378509739399912570787600662729080382999756800000000000000000000
    >>> main(-4,"!",0)
    "No es pot calcular el factorial d'un valor negatiu!"
    """
    
    if operador == "+":
        resultat = numero1 + numero2
        return resultat
    elif operador == "-":
        resultat = numero1 - numero2
        return resultat
    elif operador == "*":
        resultat = numero1 * numero2
        return resultat
    elif operador == "/":
        resultat = numero1 / numero2
        return resultat
    elif operador == "//":
        resultat = numero1 // numero2
        return resultat
    elif operador == "**":
        resultat = numero1 ** numero2
        return resultat
    elif operador == "!":
        if numero1 < 0:
            return "No es pot calcular el factorial d'un valor negatiu!"
        factorial = 1
        if numero1 > 0:
            while(numero1 > 1): 
                factorial *= numero1 
                numero1 -= 1
            return factorial
    else:
        return "El valor que has introduit no es vàlid, les operacions disponibles són: +,-,*,/,//,**,!"


if __name__ == "__main__":
    try:
        print(main(int(sys.argv[1]), sys.argv[2], int(sys.argv[3])))
    except ValueError:
        print("Has d'introduir números")
