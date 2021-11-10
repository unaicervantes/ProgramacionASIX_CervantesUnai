#!/usr/bin/python3        
# _*_ coding: utf-8 _*_   

"""
El nostre programa ha d'escriure una seqüència numèrica que comenci amb el número 'inici' i que compti de 'salt' en 'salt' fins al número 'final'
sense passar-s'hi de llarg.
"""

__author__ = "Unai Cervantes"  

import sys

def main(inici,final,salt):  
    """
    Doctest
    >>> main(10,18,2)
    '10, 12, 14, 16, 18'
    >>> main(10,17,2)
    '10, 12, 14, 16'
    >>> main(18,10,-2)
    '18, 16, 14, 12, 10'
    >>> main(-10,2,0)
    Traceback (most recent call last):
    ...
    ValueError: El valor del salt no pot ser 0
    >>> main(-10,2,3)
    '-10, -7, -4, -1, 2'
    """
    resultat = ''
    if salt == 0:
        raise ValueError ("El valor del salt no pot ser 0")   
    if salt >= 1:
        final += 1
    else:
        final -= 1
    for index in range(inici,final,salt):
        if index > inici or index < inici:
            resultat += ', ' + str(index)
        else:
            resultat += str(index)
    return resultat
if __name__ == "__main__":
    print(main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))