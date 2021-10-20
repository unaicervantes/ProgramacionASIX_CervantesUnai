#!/bin/python3
# _*_ coding: utf-8 _*_

"""
    color_quadrat.py 
    Escriu un programa que escrigui una posició com a paràmetre de la línia de comandes. 
    Utilitza un condicional 'IF' per determinar si la columna comença per un quadrat negre o blanc i desprès utilitzar aritmètica modular (operador mòdul) per 
    determinar el color de la posició. Per exemple, si l'usuari entra la posició b3 el programa ha de respondre 'blanc'. 
    Si l'usuari entra una posició no vàlida, el programa ha de respondre 'posició invàlida'.
"""

__author__ = "Unai Cervantes"

import sys
posicion = (sys.argv[1])
valor1 = posicion[0]
valor2 = int(posicion[1])
#print(valor1,valor2)
color = None
#Columna a
if valor1 == "a":
    color = "Negro"
#Columna b
elif valor1 == "b":
    color = "Blanco"
#Columna c
elif valor1 == "c":
    color = "Negro"
#Columna d
elif valor1 == "d":
    color = "Blanco"
#Columna e
elif valor1 == "e":
    color = "Negro"
#Columa f
elif valor1 == "f":
    color = "Blanco"
#Columa g
elif valor1 == "g":
    color = "Negro"
#Columna h
elif valor1 == "h":
    color = "Blanco"

if valor2 %2 == 0:
    if color=="Blanco":
        color="Negro"
    else:
        color="Blanco"
print(color)