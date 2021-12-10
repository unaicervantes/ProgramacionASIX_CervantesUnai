#!/usr/bin/python3
# _*_ coding: utf-8 _*_
import sys
n = int(sys.argv[1])
contador = 0
while contador != n:
    for quadrat in range(n):
        total = ""
        for resultat in range(0,n+1,1):       
            total += str(resultat)+" "
        print(total) 
    print("-"*n)
    contador += 1