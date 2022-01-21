#!/usr/bin/python3
# _*_ coding: utf-8 _*_

__author__="Unai Cervantes"

import sys
def main(segons):
    """
    Converteix segons a -> hores, minuts i segons
    >>> main(3)
    (0, 0, 3)
    >>> main(60)
    (0, 1, 0)
    >>> main(61)
    (0, 1, 1)
    >>> main(3727)
    (1, 2, 7)
    """
    
    hores = segons // 3600
    segons = segons % 3600
    minuts = segons // 60
    segons = segons % 60
        
    return hores, minuts, segons

if __name__ == '__main__':
    try:
        seg = int(sys.argv[1])
    except Exception as e:
        print("Has d'introduir com a paràmetre el nombre de segons que vols convertir!")
        quit()
    resultat = main(seg)
    print("Hores: " + str(resultat[0]))
    print("Minuts: " + str(resultat[1]))
    print("Segons: " + str(resultat[2]))
    