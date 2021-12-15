#!/usr/bin/python3
# _*_ coding: utf-8 _*_
import random, os

"""
barres.py mostra gràficament els elements d'una llista 
"""
__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"

def main(llista):
    """
    Visualitza gràficament els valors de llista
    >>> main([1, 2, 3])
    * 1
    ** 2
    *** 3
    >>> main([3,1,3])
    *** 3
    * 1
    *** 3
    """
    os.system('clear')
    for recorregut_llista in llista:
        for x in range(len(llista) - 1):
            for y in range(len(llista) - 1 - x):
                if llista[y] > llista[y+1]:
                    llista[y], llista[y+1] = llista[y+1], llista[y]
        print("*" * recorregut_llista,recorregut_llista)   

if __name__ == "__main__":
    vector_valors = []
    for index in range(10):
        vector_valors.append(random.randrange(30) + 1)
    main(vector_valors)