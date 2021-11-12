#!/usr/bin/python3        
# _*_ coding: utf-8 _*_   

"""
El nostre programa ha d'escriure una seqüència numèrica que comenci amb el número 'inici' i que compti de 'salt' en 'salt' fins al número 'final'
sense passar-s'hi de llarg.
"""

__author__ = "Unai Cervantes"  

import sys
def main():
    frase_lloro = None
    while frase_lloro != "":
        frase_lloro = input("L'usuari diu: ")
        if frase_lloro != "":
            print(f"El lloro diu {frase_lloro}")
if __name__ == "__main__":
    main()   