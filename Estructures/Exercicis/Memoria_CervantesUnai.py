#!/usr/bin/python3
# _*_ coding: utf-8 _*_

__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"

"""Programa que llegeix la memoria disponible/lliure/total del sistema i la escriu en una plantilla html"""

PATH_PLANTILLA = "./plantilla.html"
PATH_MEMORIA = "./memoria.html"

def llegir_dades():
    with open("/proc/meminfo") as memoria:
        total = memoria.readline()
        total = elimina_frase(total,"MemTotal:")
        lliure = memoria.readline()
        lliure = elimina_frase(lliure,"MemFree:")
        disponible = memoria.readline()
        disponible = elimina_frase(disponible,"MemAvailable:")
        
    return total,lliure,disponible


def elimina_frase(cadena,eliminar):
    cadena = cadena.replace(eliminar,"")
    cadena = cadena.strip()
    return cadena


def llegeix_plantilla(total,lliure,disponible):
    with open(PATH_PLANTILLA,"r") as plantilla:
        html = plantilla.read()
        html = html.replace("{{MTotal}}",total)
        html = html.replace("{{MDisp}}",disponible)
        html = html.replace("{{MLliure}}",lliure)
    return html

def crea_memoria(html):
    with open(PATH_MEMORIA,"w") as fitxer:
        fitxer.write(html)

def main():
    total,lliure,disponible = llegir_dades()
    crea_memoria(llegeix_plantilla(total,lliure,disponible ))
    print("El fitxer s'ha creat")
if __name__ == "__main__":
    main()