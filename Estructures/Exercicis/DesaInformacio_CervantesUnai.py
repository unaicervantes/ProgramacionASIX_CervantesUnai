#!/usr/bin/python3
# _*_ coding: utf-8 _*_

__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"

"""Exercici en el que guardarem la informació que introdueix l'usuari en un fitxer."""

"""
Justificació desar dades
------------------------
He decidit deixar les dades en un fitxer Json ja que em sembla una forma senzilla i permet guardar cada element que es demana 
de forma ordenada i fàcil d'accedir. 
Cada cop que s'inicia el programa es llegeix el fitxer de dades i es guarda en una variable. En aquesta variable s'aniran 
afegint els diferents usuaris. Es poden afegir tants usuaris com es volen en una mateixa execucció del programa. Cada cop que 
es posin les dades d'un usuari s'afegirà a la variable usuaris. Després es carregarà aquesta variable al fitxer de dades.
Com la variable conté tots els usuaris existents i nous es sobreescriurà el fitxer. 
"""

import os
import json
from time import sleep

PATH_DADES = "./dades.json"

def menu_principal():
    print("---------------------\n\
0.- Surt\n\
1.- Mostra tots els usuaris\n\
2.- Introdueix nous usuaris\n\
---------------------")


def menu_introdueix():
    print("---------------------\n\
0.- Desar usuari\n\
1.- Introduir informació\n\
---------------------")


def introdueix_opcions(comprovacio):
    dni = ""
    nom = ""
    cognom = ""
    data_naixement = ""
    telefon = ""
    opcio = None
    while opcio != 0:
        os.system("clear")
        menu_introdueix()
        opcio = int(input("Que vols fer? "))
        if opcio == 1:
            dni = input("Introdueix el DNI: ")
            nom = input("Introdueix el teu nom: ")
            cognom = input("Introdueix el teu cognom: ")
            data_naixement = input("Introdueix la teva data de naixement: ")
            telefon = input("Introdueix el teu telèfon: ")
        
        informacio = {"dni":dni,"nom":nom,"cognom":cognom,"Data_naixement":data_naixement,"Telefon":telefon}
    return informacio


def desa_dades(informacio):
    with open(PATH_DADES, "w") as outfile:
        json.dump(informacio, outfile)


def llegeix_json():
    try:
        with open(PATH_DADES, 'r') as fitxer:
            usuaris = json.load(fitxer)
        return usuaris
    except json.decoder.JSONDecodeError:
        print("No hi ha dades a mostrar.")
        sleep(2)


def main():  
    opcio = None
    while opcio != 0:
        usuaris = [llegeix_json()]
        menu_principal()
        opcio = int(input("Quina opció vols? "))
        if opcio == 1:
            os.system("clear")
            print(json.dumps(llegeix_json(), indent=4))
        elif opcio == 2:
            os.system("clear")
            informacio = introdueix_opcions(usuaris)
            usuaris.append(informacio)
            desa_dades(usuaris)


if __name__ == "__main__":
    main()