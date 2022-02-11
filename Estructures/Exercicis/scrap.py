#!/usr/bin/python3
# _*_ coding: utf-8 _*_

"""
Baixa i consulta la web de l'institut
"""

from re import A
import requests
from bs4 import BeautifulSoup

__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"

def main():
    
    url = 'https://wikipedia.es'
    web = requests.get(url)
    if web.ok:
        print("Hem llegit la pàgina correctament.")
        sopa = BeautifulSoup(web.text,'html.parser')
        etiqueta = sopa.find(id='Artículo_destacado')
        pare = etiqueta.find_parent()
        titols = sopa.find_all(class_="main-header main-box-header")
        for title in pare:
            print(title.text)
    else:
        print("Alguna cosa ha anat malament llegint la web." + str(web.status_code) + ": " + web.reason )

if __name__ == "__main__":
    main()