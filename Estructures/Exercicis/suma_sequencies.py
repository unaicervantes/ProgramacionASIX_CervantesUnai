#!/bin/python3
# _*_ coding: utf-8 _*_
"""
suma_sequencies.py suma seqüències numèriques donat l'inici i el final.
Sense paràmetres ho fa mitjançant un bucle i amb el flag -g ho fa a l'estil 
del petit Gauss.
Exemple: 
    $ python3 suma_sequencies.py 1 100
    5050

    $ python3 suma_sequencies.py -g 1 100
    5050
"""
import sys
import time

def main(comenca, termina, esEstilGauss = False):
    """
    >>> main(1, 2)
    3
    >>> main(10, 15)
    75
    >>> main(1, 100)
    5050

    >>> main(1, 2, True)
    3
    >>> main(10, 15, True)
    75
    >>> main(1, 100, True)
    5050
    """
    resultat = 0
    #Gauss
    if esEstilGauss:
        resultat = int((termina - comenca + 1)*(termina+comenca)/2)
    #Bucle
    else:
        for index in range(comenca,termina+1):
            resultat += index

    return resultat

if __name__ == "__main__":
    esRapid = False
    comenca = 0
    termina = 0
    try:
        if sys.argv[1] == '-g':
            esRapid = True
            comenca = int(sys.argv[2])
            termina = int(sys.argv[3])
        else:
            comenca = int(sys.argv[1])
            termina = int(sys.argv[2])
    except:
        print("Mode d'ús:")
        print("    >>>> python3 suma_sequencies.py [-g] 1 100 ")
        print("    5050")
    temps_inicial = time.time()
    res = main(comenca, termina, esRapid)
    temps_final = time.time()
    print(res, 1000*(temps_final -temps_inicial))



