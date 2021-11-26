#!/usr/bin/python3
# _*_ coding: utf-8 _*_


"""
Heu de realitzar un programa que imprimeixi els nombres del 1 al 110 en ordre per pantalla, però els que siguin múltiples de 3 s'han
de substituir per Blass, els que siguin múltiples de 5 per Tizz i els que siguin múltiples de 7 per Zaff. Els que siguin alhora
múltiples de 3 i de 5 han de ser substituits per BlassTizz, els que siguin múltiples de 3 i de 7 per BlassZaff, els que siguin
múltiples de 5 i de 7 per TizzZaff i els que siguin múltiples de 3, 5 i 7 per BlasTizzZaff.

"""
__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"

def main():
    for numeros in range(1,111,1):
        if numeros%3 == 0:
            if numeros%5 == 0:
                if numeros%7 == 0:
                    print("BlassTizzZaff")
                else:
                    print("BlassTizz")          
            elif numeros%7 == 0:
                print("BlassZaff")               
            else:
                print("Blass")
        elif numeros%5 == 0:
            if numeros%7 ==0:
                print("TizzZaff")
            else:
                print("Tizz")            
        elif numeros%7 == 0:
            print("Zaff")
        else:
            print(numeros)
        
        

if __name__ == "__main__":
    print(main())