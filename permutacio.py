#!/usr/bin/python3        
# _*_ coding: utf-8 _*_  

"""
Programa per permutarm paraules    
"""

__author__ = "Unai Cervantes"


import sys
frase = sys.argv[1]
frase = frase[::-1]
frase_permutada = []
for i in range(0,len(frase), 2):
    frase_permutada.append(frase[i:i+2])    
frase_permutada = frase_permutada[::-1]
frase_permutada = "".join(frase_permutada)
frase_permutada = frase_permutada[::-1]
print(frase_permutada)