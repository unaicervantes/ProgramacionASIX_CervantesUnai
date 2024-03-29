#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
Generació de cartes
"""
import random
__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"

cor     = "\U00002665"
diamant = "\U000025C6"
pica    = "\U00002660"
trevol  = "\U00002663"

COLUMNES = 13

carta = [ 
    "  ___ ", 
    "|K  |", 
    "| " + pica + " |", 
    "|__K|" 
    ]

def genera_carta(numero,simbol):
    numero = str(numero)
    carta = [ 
    " ___ ",
    "|"+ numero.ljust(3," ") +"|", 
    "| " + simbol + " |", 
    "|"+ numero.rjust(3,"_") +"|" 
    ]
    return carta 

def print_ma(ma):
    if len(ma) > COLUMNES:
        print_ma(ma[:-COLUMNES])
    resta = ma[-COLUMNES:]
    for index in range(4):
        linea = ""
        for carta in resta:
            linea += carta[index]
        print(linea)

def get_baralla():
    baralla = []
    escala = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    pals = [cor,pica,trevol,diamant]
    for index_pals in pals:
            for index_escala in escala:
                baralla.append(genera_carta(index_escala,index_pals))
    return baralla


def barreja_01(ma):
    llista = ma[:]
    for index in range(len(llista)):
        aleatori = random.randint(0, len(llista) -1)
        llista[index], llista[aleatori] = llista[aleatori], llista[index]
    return llista


def divisio_maç(ma):

    maç1 = ma[:len(ma)//2]
    maç2 = ma[len(ma)//2:]

    print("\nPrimera meitat \n----------------")
    print_ma(maç1)
    print("\nSegona meitat \n----------------")
    print_ma(maç2)
    
    maç1 = barreja_01(maç1)
    maç2 = barreja_01(maç2)
    return maç1, maç2


def fusiona(maç1,maç2):

    ma = maç1+maç2

    print("\nMaç fusionat \n--------------")
    print_ma(ma)

def main():
    #print_ma([genera_carta(10,trevol), carta, genera_carta("A", pica)])
    #print_ma(barreja_01(get_baralla()))
    maç1, maç2 = divisio_maç(barreja_01(get_baralla()))
    fusiona(maç1,maç2)

if __name__ == "__main__":
    main()