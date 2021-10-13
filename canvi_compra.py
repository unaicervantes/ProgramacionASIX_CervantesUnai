#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Exercici python per a realitzar el canvi de la compra i que retorni el número de bitllets a retornar."""

import sys

Entregat = float((sys.argv[1]))
print("Entregat:",Entregat)
Total = float((sys.argv[2]))
print("Total ticket:",Total)
Billet10 = 0
Billet5 = 0
Moneda1 = 0
Moneda05 = 0
Diferencia = (Entregat-Total)
#Billet 10
while Diferencia >= 10:
    Diferencia -= 10
    Billet10 += 1
    #print(Diferencia)
print(Billet10,"x billet de 10€")
#Billet 5
while Diferencia >= 5:
    Diferencia -= 5
    Billet5 += 1
    #print(Diferencia)
print(Billet5, "x billet de 5€")
#Moneda 1
while Diferencia >= 1:
    Diferencia -= 1
    Moneda1 += 1
    #print(Diferencia)
print(Moneda1, "x moneda de 1€")
#Moneda 0.5
while Diferencia >= 0.5:
    Diferencia -= 0.5
    Moneda05 += 1
    #print(Diferencia)
print(Moneda05,"x moneda de 0.5€")
print("--------------------")
print("Total de canvi:",(Entregat-Total),"€")