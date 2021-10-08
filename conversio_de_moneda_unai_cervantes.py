#!/usr/bin/python3

tipus_moneda = input("A quina moneda vols convertir els teus Euros?")
equivalent = float(input("Quina quantitat d'aquesta moneda és equivalent a 1 EUR?"))
quantitat = int(input("Quants euros vols canviar?"))
quantitat = float(quantitat)
canvi = equivalent * quantitat
print("L'equivalent de", quantitat, "es de", canvi, tipus_moneda)