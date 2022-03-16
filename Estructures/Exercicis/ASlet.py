#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import os

__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"

def mostra_menu():
    print("0.- Surt de l'aplicació\n\
1.- Entrar paraula secreta\n\
2.- Endevinar paraula secreta")

def endevinar_paraula(paraula_secreta):
    llista = []
    paraula = input("Introdueix la paraula que creus que es: ")
    if paraula == paraula_secreta:
        return "Correcte" 
    print(paraula)
    for index in range(len(paraula_secreta)):
        if paraula_secreta[index] == paraula[index]:
            print("V",end="")
        else:
            if paraula[index] in paraula_secreta:
                print("O",end="")
            else:
                print("X",end="")
    print("",end="\n")

def paraula_a_endevinar():
    paraula_secreta = input("Introdueix la paraula a endevinar: ")
    if len(paraula_secreta) > 5 or len(paraula_secreta) < 5:
        os.system("clear")
        print("La paraula secreta ha de tenir cinc lletres.")
    return paraula_secreta

def main():
    opcio = None
    while opcio != 0:
        mostra_menu()
        opcio = int(input("Selecciona una opció: "))
        if opcio == 1:
            paraula_secreta = paraula_a_endevinar()
        elif opcio == 2:
            resultat = endevinar_paraula(paraula_secreta)
            if resultat == "Correcte":
                return "Paraula correcte!"

if __name__ == "__main__":
    print(main())