#!/usr/bin/python3
# _*_ coding: utf-8 _*_

__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"

import sys 

def main(numero1,operador,numero2):

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
        for index in range(numero1,0,-1):
            print(index)


if __name__ == "__main__":
    print(main(int(sys.argv[1]), sys.argv[2], int(sys.argv[3])))