#!/usr/bin/python3        
# _*_ coding: utf-8 _*_   

"""
Aquest programa encripta missatges de text passant-li com a primer paràmetre la clau d'encriptació 
i com a segon paràmetre el paràmetre a encriptar.    
"""

__author__ = "Unai Cervantes"  

import sys
def main(clau,frase):
    """
    >>> main('13213121','Hola Mundo!')
    m:ñaNvb?mjG
    """
    pass

    if len(sys.argv) > 3:
        print("Es necessiten dos paràmetres")
        quit()
    if len(sys.argv) < 3:
        print("Es necessiten dos paràmetres<")
        quit()
    clau = sys.argv[1]
    frase = sys.argv[2]
    #print(clau,frase)
    frase = frase[::-1]
    #print(frase)
    frase_permutada = []
    for i in range(0,len(frase), 2):
        frase_permutada.append(frase[i:i+2])   
    #print(frase_permutada) 
    frase_permutada = frase_permutada[::-1]
    #print(frase_permutada)
    frase_permutada = "".join(frase_permutada)
    #print(frase_permutada)
    frase_permutada = frase_permutada[::-1]
    #print(frase_permutada)
    grup1 = ["a","b","c","d"]
    grup2 = ["e","f","g","h"]
    grup3 = ["i","j","k","l"]
    grup4 = ["m","n","ñ","o"]
    grup5 = ["p","q","r","s"]
    grup6 = ["t","u","v","w"]
    grup7 = ["x","y","z","."]
    grup8 = ["?","!"]
    grups = [["a","b","c","d"],["e","f","g","h"],["i","j","k","l"],["m","n","ñ","o"],["p","q","r","s"],["t","u","v","w"],["x","y","z","."],["?","!"]]
    contador = 0
    posicion = 0
    llista_clau = list(clau)
    #print(llista_clau[0])

    for s in llista_clau:
        valor = grups.index("h")
        print(grups[1])
        
"""
    while contador != llista_clau[0]:
        letra = grup1[posicion]
        posicion+= 1
        contador+= 1
        print (contador)
        print(f"Esto es la posicion {posicion}")
        print(letra)
        if posicion == 4:
            posicion = 0
        print (f"Esto es la posicion después del if {posicion}")
        print(f"Esto es la letra final {letra}")"""

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])