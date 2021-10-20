#!/bin/python3
# _*_ coding: utf-8 _*_

"""
    edat_gos.py
    Donada l'edat natural d'un gos en anys 
    naturals i ens calcula la seva edat de gos 
    equivalent a la nostra edad humana
"""

__author__ = "Unai Cervantes"

import sys

if len(sys.argv) < 2:
    print(" \
No has informat de l'edat relativa del gos.\n \
Ús:\n \
$ python3 edat_gos.py 3\n \
3 anys humans equivalen a 25 anys de gos. \
    ")
    quit()

edat_natural_gos = int(sys.argv[1])
edat_relativa_gos = 0

if edat_natural_gos < 3:
    edat_relativa_gos = edat_natural_gos * 10.5
else:
    edat_relativa_gos = 21 + (edat_natural_gos - 2) * 4

print(f"{edat_natural_gos} anys humans equivalent \
a {edat_relativa_gos} anys de gos")