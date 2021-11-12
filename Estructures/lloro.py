#!/usr/bin/python3        
# _*_ coding: utf-8 _*_   

"""
Quan l'usuari entri la seva frase, el programa ha de'escriure "El lloro repeteix: <frase escrita per l'usuari>" 
i ha de tornar a escriure en una altra línia "L'usuari diu: " i tornar a esperar que l'usuari escrigui la seva frase.
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