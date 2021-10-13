#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Exercici python per a realitzar el canvi de la compra i que retorni el número de bitllets a retornar.s"""

import sys

Entregat = float((sys.argv[1]))
print("Entregat:",Entregat)
Total = float((sys.argv[2]))
print("Total ticket:",Total)
Billet10 = 0
Billet5 = 0
Moneda1 = 0
Moneda05 = 0
Llista = [Billet10,Billet5,Moneda1,Moneda05]
Valors = [10,5,1,0.5]
Diferencia = (Entregat-Total)
for valors_for in Valors:
    #print(valors_for)
    for llista_for in Llista:
        continue
    #print(llista_for)
    while Diferencia >= valors_for:
        Diferencia -= valors_for
        llista_for += 1
    print(llista_for,"x bitllet de",valors_for,"€")
print("--------------------")
print("Total de canvi:",(Entregat-Total),"€")