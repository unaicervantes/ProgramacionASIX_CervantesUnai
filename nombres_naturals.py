#!/usr/bin/python3

llista = []
nombre_natural = -1
suma = 0
while nombre_natural != 0:
    nombre_natural = int(input("Escriu nombre naturals o un 0 per a finalitzar: "))
    if nombre_natural != 0:
        llista.append(nombre_natural)
for i in llista:
    suma+= i
valor_mig = suma/len(llista)
print("La llista es:",llista,"El valor mig es:", valor_mig)
