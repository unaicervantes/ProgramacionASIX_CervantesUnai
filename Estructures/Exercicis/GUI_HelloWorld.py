#!/usr/bin/python3
# _*_ coding: utf-8 _*_

__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"

import tkinter

def click_boto():
    finestra = ""
    etiqueta = tkinter.Label(finestra, text=f"Hola {entrada.get()}!")
    etiqueta.pack()


finestra = tkinter.Tk()
etiqueta = tkinter.Label(finestra,text="Hola mundo!")
etiqueta.pack()
entrada = tkinter.Entry(finestra,width=60)
entrada.pack()
entrada.insert(0,"Escriu el teu nom: ")

un_boto = tkinter.Button(finestra,text="Fes clic!",padx=10, pady=10, fg="blue", command=click_boto)
un_boto.pack()

finestra.mainloop()
print("Hem tancat la finestra")

"""if __name__ == "__main__":
    main()"""