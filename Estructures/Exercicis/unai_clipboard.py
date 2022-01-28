#!/usr/bin/python3
# _*_ coding: utf-8 _*_

__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"

from tkinter.messagebox import RETRYCANCEL
import clipboard
import json
import sys

"""
Jugant amb clipboard
"""

RUTA_FITXER = "/tmp/org.joandaustria.json"

def recupera_valors():
    try:
        with open(RUTA_FITXER,"r") as f:
            valors = json.loads(f.read())
            return valors
    except:
        with open(RUTA_FITXER,"w") as f:
            f.write('{}')
            return {}

def desa(clau, valor):
    historic_de_valors = recupera_valors()
    historic_de_valors[clau] = valor
    with open(RUTA_FITXER, "w") as f:
        f.write(json.dumps(historic_de_valors))

def main(comand, key):
    if comand == 'save':
        desa(key, clipboard.paste())
        return "Objecte desat amb contingut: " + clipboard.paste()
    elif comand == 'restore':
        valor_desat = recupera_valors()[key]
        clipboard.copy(valor_desat)
        return "Objecte recuperat amb contigut: " + valor_desat
    else:
        return json.dumps(recupera_valors(), sort_keys=True, indent=4)

if __name__ == "__main__":
    #python3 unai_clipboard [save|restore|list]
    comanda = None
    clau = None
    try:
        comanda = sys.argv[1]
        if not (comanda == "list"):
            clau = sys.argv[2]
        print(main(comanda,clau))
    except Exception as e:
        print("Mode de ús:")
        print("\tpython3 unai_clipboard [save|restore|list] [clau]")
