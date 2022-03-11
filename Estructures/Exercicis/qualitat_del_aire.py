#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
qualitat_del_aire.py

Programa que fa consultes a l'API de mesures automàtiques de contaminants de l'aire a Catalunya

Components del grup:
    - Unai Cervantes
    - Jerry Flores 

https://analisi.transparenciacatalunya.cat/resource/tasf-thgu.json
"""

import requests
import json

def menu():
    print("0.- Surt de l'aplicació\n\
1.- Filtra per municipi\n\
2.- Filtra per contaminant\n\
3.- Mostra dades filtrades, esborra filtres i refresca dades")

def processa_opcio(opcio,dades):
    if opcio == "1":
        dades = filtrar_municipi(dades)
    elif opcio == "2":
        dades = filtrar_contaminant(dades)
    elif opcio == '3':
        for dada in dades:
            print_dada(dada)       
        dades = refresca_dades()

    return dades

def refresca_dades():
    dades = requests.get("https://analisi.transparenciacatalunya.cat/resource/tasf-thgu.json").json()
    return dades

def filtrar_municipi(dades):
    municipi = input("Per quin municipi vols filtar? ")
    dades = list(filter(lambda x: x["municipi"].lower() == municipi,dades))
    return dades

def filtrar_contaminant(dades):
    contaminant = input("Per quin contaminant vols filtar? ")
    dades = list(filter(lambda x: x["contaminant"].lower() == contaminant,dades))
    return dades

def getNomContaminant(contaminant):
    """
    >>> getNomContaminant("O3")
    'Ozò'
    >>> getNomContaminant("CO")
    'Monòxid de carboni'
    >>> getNomContaminant("PM3")
    ''
    """
    noms_contaminants = {"O3": "Ozò", "PM10": "Partícules menors 10 micròmetres", 
                        "NO2": "Diòxid de nitrògen", "NO": "Òxid de nitrògen", "NOX": "Òxids de nitrògen", 
                        "SO2": "Diòxid de Sofre", "CO": "Monòxid de carboni"}
    try:
        return noms_contaminants[contaminant]
    except:
        return ""


def print_dada(dada):
    print(f"|--- Estació: {dada['nom_estacio']}")
    print(f"|->    magnitud: {dada['magnitud']}")
    print(f"|->    contaminant: {dada['contaminant']}: {getNomContaminant(dada['contaminant'])}")
    print(f"|->    unitats: {dada['unitats']}")
    print(f"|->    data: {dada['data']}")
    print()


def main():
    opcio = ""       
    dades = refresca_dades()
    while opcio != "0":
        menu()
        opcio = input("Tria una opció: ")  
        dades = processa_opcio(opcio,dades)
        

    #dades = list(filter(lambda x: x["municipi"].lower() == "viladecans",dades))
    #dades = list(filter(lambda x: x["contaminant"].lower() == "o3",dades))
    #for dada in dades:
     #   print_dada(dada)


if __name__ == "__main__":
    main()