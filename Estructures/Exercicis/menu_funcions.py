#!/bin/python3
# _*_ coding: utf-8 _*_

"""
menu.py
Example de menú en la terminal
"""

import json
import qrcode

__author__ = "Unai Cervantes"
__email__ = "cf19unai.cervantes@iesjoandaustria.org"
__license__ = "GPL Vk3"

def llistat_menu():
    print("                                    ")
    print("***********************************")
    print("|-> 0. Sortir")
    print("|-> 1. Afegir nova parella clau-valor")
    print("|-> 2. Veure lla llista de parelles")
    print("|-> 3. Crear codi QR")
    print("***********************************")
    print("                                    ")

def sel_opcio():
    return input("Selecciona una de les opcions: ")

def opcions_menu(opcio,magatzem):

    if opcio == "0":
        print("Fins aviat!")
    elif opcio == "1":
        clau = input("Quina clau vols utilitzar?: ")
        valor = input("Quin valor vols desar?: ")
        magatzem[clau] = valor
        input("[Enter]")
    elif opcio == "2":
        print(magatzem)
        input("[Enter]")
    elif opcio == "3":
        text = json.dumps(magatzem, indent=4)
        print(text)
        input("[Enter]")
        path = '/tmp/org.iejsoandaustria.qrcode.png'
        img = qrcode.make(text)
        img.save(path)
        print(path)
    else:
        print("Oops! Opció incorrecta")

def main():
    opcio = sel_opcio
    magatzem = {}    
    while (opcio != "0"):
        llistat_menu()
        opcio = sel_opcio()
        opcions_menu(opcio,magatzem)

if __name__ == "__main__":
    main()