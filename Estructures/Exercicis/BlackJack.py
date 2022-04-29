#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
from curses.ascii import isdigit
import random
import functools
from functools import reduce
from time import sleep
import os

 
cor     = "\U00002665"
diamant = "\U000025C6"
pica    = "\U00002660"
trevol  = "\U00002663"


PALS = [cor, diamant, pica, trevol]
FIGURES = ["J", "Q", "K", "A"]
COLUMNES = 13


def print_ma(ma):
    if len(ma) > COLUMNES:
        print_ma(ma[:-COLUMNES])
    fila = ma[-COLUMNES:]
    for linea in range(4):
        resultat = ""
        for carta in fila:
            resultat = resultat +  carta[linea]
        print(resultat)
    return


def genera_carta(n, pal):
    return [
        " " + ("_"*3) + " ",
        "|" + f"{str(n):3}" + "|",
        "|" + pal.center(3) + "|",
        "|" + str(n).rjust(3,"_") + "|"
    ]
    

def genera_baralla():
    resultat = []
    for pal in PALS:
        for carta in genera_conjunt_pal(pal):
            resultat.append(carta)
    return resultat
    

def divideix_maç(maç):
    tall = len(maç)//5
    tall += random.randint(0, len(maç)//2)
    if tall > len(maç):
        tall = len(maç)
    return maç[:tall], maç[tall:]


def fusiona(a, b):
    resultat = []
    len_gran = len(a) if len(a) > len(b) else len(b)
    for index in range(len_gran):
        if len(a):
            resultat.append(a.pop(0))
        if len(b):
            resultat.append(b.pop(0))
    return resultat

def barreja_01(maç):
    return fusiona(*divideix_maç(maç))


def barreja_02(maç):
    a, b = divideix_maç(maç)
    c, d = divideix_maç(a)
    e, f = divideix_maç(b)
    a = fusiona(c ,e)
    b = fusiona(d, f)
    return fusiona(a, b)


def barreja_03(maç):
    resultat = []
    for i in range(len(maç)):
        resultat.append(maç[i])
    for i in range(len(resultat)):
        origen = random.randint(0, len(resultat) - 1)
        desti = random.randint(0, len(resultat) - 1)
        resultat[origen], resultat[desti] = resultat[desti], resultat[origen]
    return resultat

def genera_conjunt_pal(pal):
    resultat = []
    for n in range(2,11):
        resultat.append(genera_carta(n, pal))
    for f in FIGURES:
        resultat.append(genera_carta(f, pal))
    return resultat


def get_valor_carta(carta):
    """
    >>> get_valor_carta(genera_carta(3, cor))
    3
    >>> get_valor_carta(genera_carta('J', cor))
    10
    >>> get_valor_carta(genera_carta('Q', cor))
    10
    >>> get_valor_carta(genera_carta('K', cor))
    10
    >>> get_valor_carta(genera_carta('A', cor))
    11
    >>> get_valor_carta(genera_carta('10', cor))
    10
    >>> get_valor_carta(genera_carta('2', cor))
    2
    """
    valor = carta[1].strip("|").strip()
    if valor.isdigit():
        return int(valor)
    if valor == 'A':
        return 11
    return 10


def get_valors_ma(ma):
    """
    >>> ma = [genera_carta(3, cor), genera_carta(4, trevol)]
    >>> get_valors_ma(ma)
    [3, 4]
    >>> ma.append(genera_carta('J', cor))
    >>> get_valors_ma(ma)
    [3, 4, 10]
    >>> ma.append(genera_carta('A', cor))
    >>> get_valors_ma(ma)
    [3, 4, 10, 11]
    """
    resultat = []
    for index in ma:
        resultat.append(get_valor_carta(index))
    return resultat


def suma_valors_ma(valors):
    """
    · Utilitzar la funció reduce.
    · No modificar el contingut del paràmetre d'entrada valors.
    >>> suma_valors_ma([2, 10, 5])
    17
    >>> suma_valors_ma([2, 10, 11])
    13
    >>> suma_valors_ma([11, 10, 2])
    13
    >>> suma_valors_ma([11, 10])
    21
    >>> suma_valors_ma([10, 11])
    21
    >>> suma_valors_ma([11, 11])
    2
    """
    total = reduce(lambda x,y: x+y,valors)
    if total > 21:
        for index in valors:
            if index == 11:
                total -= 10
    return total

def mostra_menu():
    print("---------------------\n\
0.- Surt\n\
1.- Demana\n\
2.- Plantat\n\
3.- Reinicia\n\
---------------------")

def baralla_barrejada():
    baralla = genera_baralla()
    baralla_b = barreja_03(baralla)
    baralla_b = barreja_01(baralla_b)
    baralla_b = barreja_02(baralla_b)
    baralla_b = barreja_03(baralla_b)
    return baralla_b

def main():
    opcio = None
    valors = []
    puntuacio = 0
    ma= []
    baralla = baralla_barrejada()

    while opcio != 0:
        mostra_menu()
        opcio = int(input("Que vols fer? "))
        if opcio == 1:
            ma.append(baralla.pop())
            print_ma(ma)
            valors = get_valors_ma(ma)
            puntuacio = suma_valors_ma(valors)
            print(f"Valors: {valors} puntuació: {puntuacio}\n")

        elif opcio == 2:
            os.system("clear")
            print("Aquestes son les teves cartes\n-----------------------------")
            print_ma(ma)
            print(f"\nValors: {valors} puntuació: {puntuacio}\n")
            opcio = 0
            
        elif opcio == 3:
            valors = []
            puntuacio = 0
            ma = []
            baralla = baralla_barrejada()


if __name__ == "__main__":
    main()