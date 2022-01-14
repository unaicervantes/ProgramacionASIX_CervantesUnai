#!/usr/bin/python3
# _*_ coding: utf-8 _*_

__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"

def main():
    opcio = None
    while opcio != 0:
        print("--- --- --- --- --- --- --- --- --- --- --- ---\n\
0.- Surt del programa.\n\
1.- Tot amb majúscules.\n\
2.- Tot amb minúscules.\n\
3.- Inverteix l'ús de majúscules i minúscules.\n\
4.- Majúscula la primera lletra de cada paraula.\n\
    --- --- --- --- --- --- --- --- --- --- --- ---")
        opcio = int(input("Selecciona una opció: "))
        if opcio >=5:
            print("Opcio incorrecta. Hi han 5 opcions (0-4)") 

        if opcio == 0:
            quit()
        
        elif opcio == 1:
            print("Has triat tot amb majúscules")
            frase = input("Introdueix la frase a processar: ") 
            frase_canviada = frase.upper()
            print (f"<<<{frase_canviada}>>>")

        elif opcio == 2:
            print("Has triat tot amb minúscules")
            frase = input("Introdueix la frase a processar: ")
            frase_canviada = frase.lower()
            print (f"<<<{frase_canviada}>>>") 

        elif opcio == 3:
            print("Has triat invertir l'ús de majúscules i minúscules")
            frase = input("Introdueix la frase a processar: ")
            frase_canviada = frase.swapcase()
            print (f"<<<{frase_canviada}>>>") 

        elif opcio == 4:
            print("Has triat posar en majúscula la primera lletra de cada paraula")
            frase = input("Introdueix la frase a processar: ") 
            frase_canviada = frase.title()
            print (f"<<<{frase_canviada}>>>")

if __name__ == "__main__":
    main()