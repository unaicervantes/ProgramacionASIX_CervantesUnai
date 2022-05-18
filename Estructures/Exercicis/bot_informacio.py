#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys        # Permet capturar els paràmetres de la línia de comandes
import requests   # Enviar peticions HTTP de forma sencilla
import json       # Codificar en format JSON

__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"

"""
Enviarà un missatge a discord si la memòria disponible es inferior a la meitat.
"""
ganxo = 'https://discord.com/api/webhooks/976504155092975687/fqEOMfHAnmLh3xZ6_22lZTWEt31Otl7lk32dzeD2luYtqb8OfBg3wBqc9KXi4H1A8JOZ'


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
    cadena = cadena.replace("kB","")
    cadena = cadena.strip()
    return cadena

def comprova_memoria():
    total,lliure,disponible =llegir_dades()
    if int(total)//int(lliure) < 0.5:
        return True

def main(ganxo):
    missatge = "La memòria es inferior a la meitat"
    resultat = "[X] Alguna cosa ha anat malament! :(  "
    capcaleres = {'Content-Type': 'application/json'}
    carrega = {"content": missatge}
    if comprova_memoria() == True:
        resposta = requests.post(
            ganxo, 
            data=json.dumps(carrega), 
            headers=capcaleres
            )
        if resposta.ok:
            resultat = "Missatge enviat"
        else:
            resultat = resultat + str(resposta.status_code ) + ": " + resposta.reason
    else:
        print("No lo es")
    
    return resultat


if __name__ == "__main__":
    print(main(ganxo))