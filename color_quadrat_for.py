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
letras = ("a","b","c","d","e","f","g","h")
dicc = {"a":"Negro","b":"Blanco","c":"Negro","d":"Blanco","e":"Negro","f":"Blanco","g":"Negro","h":"Blanco"}
while True:
    for lista_letras in letras:
        
        if valor1 == lista_letras:
            #print (dicc[lista_letras])
            color = (dicc[lista_letras])
    break

if valor2 %2 == 0:
    if color=="Blanco":
        color="Negro"
    else:
        color="Blanco"
print(color)