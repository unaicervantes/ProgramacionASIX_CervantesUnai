#!/usr/bin/python3
# _*_ coding: utf-8 _*_

"""
Ordenació de valors.
"""
__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"

def main():
    nombre_usuari = 0
    valors_vector = []
    while (nombre_usuari >= 0):
        try:
            nombre_usuari = (int(input("Escriu un nombre, un negtaiu per acabar: ")))
        except:
            nombre_usuari = -1
        if nombre_usuari >= 0:
            valors_vector.append(nombre_usuari)
    print(f"\nEl vector sense ordenar: \n{valors_vector}")
    for iteracio in range(len(valors_vector) -1):
        for comptador in range (len(valors_vector) -1):
            if valors_vector[comptador] > valors_vector[comptador + 1]:
                valors_vector[comptador] , valors_vector[comptador + 1] = valors_vector[comptador + 1], valors_vector[comptador]

    print(f"\nEl vector ordenat: \n{valors_vector}")
if __name__ == "__main__":
    main()