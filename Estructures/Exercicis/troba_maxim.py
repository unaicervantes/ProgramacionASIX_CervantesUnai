#!/usr/bin/python3
# _*_ coding: utf-8 _*_

"""
troba_maxim.py rep números naturals de forma seqüencial i termina al rebre un de negatiu.
Al terminar informa de quin ha estat el nombre més gran introduït.
"""
__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"

def main():
    llista_total_valors = [] 
    valor_actual = 1
    while valor_actual >= 0:
        valor_actual = int(input("Introdueix un número natural: "))
        if valor_actual > 0:
            llista_total_valors.append(valor_actual)
        maxim = max(llista_total_valors)
    return maxim

if __name__ == "__main__":
    print(f"El màxim ha estat: {main()}")
