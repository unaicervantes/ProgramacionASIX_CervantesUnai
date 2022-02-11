#!/usr/bin/python3
# _*_ coding: utf-8 _*_

__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"

import json
import requests

def main():
    contingut = input("Introduexi el contingut: ")
    data={'content':contingut}
    url = "https://discord.com/api/webhooks/941718525372940328/C4zoqowS5LcgmnJycBQkHCZ_Xks5TaVrVYkIzszBA37_Rk5X7Jp4GcZUJ2FfcrqHnTJh"
    enviament = requests.post (url,json=data)
    if enviament.ok:
        print("El missatge s'ha enviat.")
    else:
        print("No s'ha pogut enviar el missatge.")

if __name__ == "__main__":
    main()