#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
"""
Exemple d'implementació multillengua a partir del 
programa que permet desar de forma persistent i desprès recuperar dades d'usuaris.
"""

__author__ = "Unai Cervantes"
__license__ = "GPL3"

PATH_DADES = "./dades.txt"
PATH_TEXTOS = "./multilingue_resources.json"
IDIOMA_DEFAULT = "ca"
IDIOMES = {
    "ca": "català", 
    "es": "español", 
    "en": "english"
    }

textos_multilingues = {}
usuaris = []


def show_menu():
    print(f"0. {textos_multilingues['sortir']}")
    print(f"1. {textos_multilingues['llegir_usuaris']}")
    print(f"2. {textos_multilingues['afegir_usuari']}")
    print(f"3. {textos_multilingues['canviar_idioma']}")


def llegir_usuaris():
    global PATH_DADES
    global usuaris
    try:
        with open(PATH_DADES, 'r') as f:
            usuaris = json.loads(f.read())
    except FileNotFoundError:
        pass


def get_textos(path, idioma):
    with open(path, 'r') as f:
        textos = json.load(f)     
        if idioma == textos[0]["codi"]:
            textos = textos[0]["textos"]
            return textos
        elif idioma == textos[1]["codi"]:
            textos = textos[1]["textos"]
            return textos
        else:
            textos = textos[2]["textos"]
            return textos


def mostrar_usuaris():
    global usuaris
    llegir_usuaris()
    print(json.dumps(usuaris, sort_keys=True, indent=2))


def mostra_posibles_idiomes():
    for idioma in IDIOMES:
        print(f"{idioma}: {IDIOMES[idioma]}")


def canvia_idioma():
    global textos_multilingues
    mostra_posibles_idiomes()

    idioma = input("Quin idioma vols? ")
    textos_multilingues = get_textos(PATH_TEXTOS,idioma)
        

def afegir_usuari():
    llegir_usuaris()
    dni = input("Introdueix DNI: ")
    nom = input("Introdueix nom: ")
    cognom = input("Introdueix cognom: ")
    telefon = input("Introdueix telèfon: ")
    usuari_desat = list(filter(lambda u : u["dni"] == dni, usuaris))
    
    if len(usuari_desat) > 0:
        selected_user = usuari_desat[0]
        selected_user["nom"] = nom
        selected_user["cognom"] = cognom
        selected_user["telefon"] = telefon
    else:
        usuaris.append({"dni": dni, "nom": nom, "cognom": cognom, "telefon": telefon})
    
    with open(PATH_DADES, 'w') as f:
        f.write(json.dumps(usuaris))


def procesa_opcio(option):
    return {
        "0": lambda : print("Fins aviat!"),
        "1": mostrar_usuaris,
        "2": afegir_usuari,
        "3": canvia_idioma
    }.get(option, lambda : print(f"{textos_multilingues['seleccio_dolenta']}"))    


def main():
    option = None
    global textos_multilingues
    textos_multilingues = get_textos(PATH_TEXTOS, IDIOMA_DEFAULT)
    while option != "0":
        show_menu()
        option = input("Selecciona una opció: ")
        procesa_opcio(option)()


if __name__ == "__main__":
    main()
