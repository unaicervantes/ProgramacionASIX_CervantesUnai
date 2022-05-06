#!/usr/bin/python3
# _*_ coding: utf-8 _*_

__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"

"""Exercici en el que guardarem la informació que introdueix l'usuari en un fitxer."""

import os
import json

PATH_DADES = "./dades.json"

def menu_principal():
    print("---------------------\n\
0.- Surt\n\
1.- Mostra tots els usuaris\n\
2.- Introdueix nous usuaris\n\
---------------------")


def menu_introdueix():
    print("---------------------\n\
0.- Continua\n\
1.- DNI\n\
2.- Nom\n\
3.- Cognom\n\
4.- Data naixement\n\
5.- Telèfon\n\
---------------------")


def introdueix_opcions():
    dni = ""
    nom = ""
    cognom = ""
    data_naixement = ""
    telefon = ""
    opcio = None
    while opcio != 0:
        os.system("clear")
        menu_introdueix()
        opcio = int(input("Quina dada vols introduir? "))
        if opcio == 1:
            dni = input("Introdueix el DNI: ")
            if dni in llegeix_json():
                input("Aquest DNI no està permes, torna'l a introduir: ")
        elif opcio == 2:
            nom = input("Introdueix el teu nom: ")
        elif opcio == 3:
            cognom = input("Introdueix el teu cognom: ")
        elif opcio == 4:
            data_naixement = input("Introdueix la teva data de naixement: ")
        elif opcio == 5:
            telefon = input("Introdueix el teu telèfon: ")
    informacio = {"dni":dni,"nom":nom,"cognom":cognom,"Data_naixement":data_naixement,"Telefon":telefon}
    return informacio


def desa_dades(informacio):
    with open(PATH_DADES, "w") as outfile:
        json.dump(informacio, outfile)


def llegeix_json():
    with open(PATH_DADES, 'r') as fitxer:
        usuaris = json.load(fitxer)
    return usuaris


def main():
    usuaris = (llegeix_json())
    opcio = None
    while opcio != 0:
        menu_principal()
        opcio = int(input("Quina opció vols? "))
        if opcio == 1:
            os.system("clear")
            print(json.dumps(llegeix_json(), indent=4))
        elif opcio == 2:
            os.system("clear")
            informacio = introdueix_opcions()
            usuaris.append(informacio)
            desa_dades(usuaris)


if __name__ == "__main__":
    main()