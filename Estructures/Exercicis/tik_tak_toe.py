#!/usr/bin/python3
# _*_ coding: utf-8 _*_
import random, os, functools

"""
tik_tak_toe.py mostra un taulell de tik-tak-toe i comprova si te un guanyador
"""
__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"


def dibuixa_taulell(board):
    """
    >>> print(dibuixa_taulell([[1,1,1],[1,1,1],[1,1,1]]))
    |X|X|X|
    |X|X|X|
    |X|X|X|
    <BLANKLINE>
    """
    representacio_taulell = ""
    simbols = [" ", "X", "O"] 
    for index in board:
        a1 = simbols[index[0]]
        a2 = simbols[index[1]]
        a3 = simbols[index[2]]
        print(f"|{a1}|{a2}|{a3}|")


    return representacio_taulell


def comproba_guanyador(taulell):
    """
    # Comprova diagonal 1
    >>> print(comproba_guanyador([[1,0,2],[0,1,2],[2,0,1]]))
    Ha guanyat el jugador 1

    # Comprova diagonal 2
    >>> print(comproba_guanyador([[1,1,2],[0,2,2],[2,1,1]]))
    Ha guanyat el jugador 2

    # Comprova linia 1
    >>> print(comproba_guanyador([[1,1,1],[0,2,2],[2,0,0]]))
    Ha guanyat el jugador 1

    # Comprova linia 3
    >>> print(comproba_guanyador([[1,0,1],[0,0,1],[2,2,2]]))
    Ha guanyat el jugador 2

    # Comprova columna 1
    >>> print(comproba_guanyador([[1,0,2],[1,0,2],[1,2,0]]))
    Ha guanyat el jugador 1

    # Comprova quan no hi ha guanyador
    >>> print(comproba_guanyador([[0,0,0],[0,0,0],[1,2,0]]))
    <BLANKLINE>
    """
    #diagonal1
    comptador = 0
    diagonal1 = []
    resultat = ""
    for index in taulell:
        diagonal1.append(index[comptador])
        comptador = comptador + 1

    
    if diagonal1 == [1,1,1]:
        resultat = "Ha guanyat el jugador 1"
        return resultat
    elif diagonal1 == [2,2,2]:
        resultat = "Ha guanyat el jugador 2"
        return resultat
    else:
        resultat = "No diagonal1"

    #diagonal2
    comptador = 2
    diagonal2 = []
    resultat = ""
    for index_dia2 in taulell:
        diagonal2.append(index_dia2[comptador])
        comptador = comptador - 1
    
    if diagonal2 == [1,1,1]:
        resultat = "Ha guanyat el jugador 1"
        return resultat
    elif diagonal2 == [2,2,2]:
        resultat = "Ha guanyat el jugador 2"
        return resultat
    else:
        resultat = "No diagonal2"
    
    #Linias
    comptador = 0
    for index_linia in taulell:
        if index_linia == [1,1,1]:
            resultat = "Ha guanyat el jugador 1"
            return resultat
        elif index_linia == [2,2,2]:
            resultat = "Ha guanyat el jugador 2"
            return resultat
        comptador = comptador + 1
        
    
    #Columna1
    comptador = 0
    columna1 = []
    resultat = ""
    for index_c1 in taulell:
        columna1.append(index_c1[comptador])

    if columna1 == [1,1,1]:
        resultat = "Ha guanyat el jugador 1"
        return resultat
    elif columna1 == [2,2,2]:
        resultat = "Ha guanyat el jugador 2"
        return resultat
    else:
        resultat = "No diagonal1"

    #Columna2
    comptador = 1
    columna2 = []
    resultat = ""
    for index_c2 in taulell:
        columna2.append(index_c2[comptador])

    if columna2 == [1,1,1]:
        resultat = "Ha guanyat el jugador 1"
        return resultat
    elif columna2 == [2,2,2]:
        resultat = "Ha guanyat el jugador 2"
        return resultat
    else:
        resultat = "No diagonal1"
    
    #Columna3
    comptador = 2
    columna3 = []
    resultat = ""
    for index_c3 in taulell:
        columna3.append(index_c3[comptador])

    if columna3 == [1,1,1]:
        resultat = "Ha guanyat el jugador 1"
        return resultat
    elif columna3 == [2,2,2]:
        resultat = "Ha guanyat el jugador 2"
        return resultat
    else:
        resultat = "No diagonal1"
    
    return " "
    
def main(taulell):
    """
    Dibuixa el taulell i comprova si hi ha guanyadors
    # Comprova diagonal 1
    >>> print(main([[1,0,2],[0,1,2],[2,0,1]]))
    |X| |O|
    | |X|O|
    |O| |X|
    Ha guanyat el jugador 1

    # Comprova diagonal 2
    >>> print(main([[1,1,2],[0,2,2],[2,1,1]]))
    |X|X|O|
    | |O|O|
    |O|X|X|
    Ha guanyat el jugador 2

    # Comprova linia 1
    >>> print(main([[1,1,1],[0,2,2],[2,0,0]]))
    |X|X|X|
    | |O|O|
    |O| | |
    Ha guanyat el jugador 1

    # Comprova linia 3
    >>> print(main([[1,0,1],[0,0,1],[2,2,2]]))
    |X| |X|
    | | |X|
    |O|O|O|
    Ha guanyat el jugador 2

    # Comprova columna 1
    >>> print(main([[1,0,2],[1,0,2],[1,2,0]]))
    |X| |O|
    |X| |O|
    |X|O| |
    Ha guanyat el jugador 1

    # Comprova quan no hi ha guanyador
    >>> print(main([[0,0,0],[0,0,0],[1,2,0]]))
    | | | |
    | | | |
    |X|O| |
    <BLANKLINE>
    """
    resultat = dibuixa_taulell(taulell)
    resultat = resultat + comproba_guanyador(taulell)
    return resultat
    


if __name__=="__main__":
    taulell_tik_tak_toe = [
        [2,1,1],
        [1,2,1],
        [1,0,2]
    ]
    print(main(taulell_tik_tak_toe))