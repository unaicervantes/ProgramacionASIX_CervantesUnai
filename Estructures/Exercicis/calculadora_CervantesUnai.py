#!/usr/bin/python3
# _*_ coding: utf-8 _*_

__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"

from glob import glob
from inspect import Parameter
from ossaudiodev import SOUND_MIXER_DIGITAL2
import tkinter
valor_en_pantalla = 0
valor1 = 0
operacio = ""
def click_boto(digit):
    global valor_en_pantalla
    valor_en_pantalla *= 10
    valor_en_pantalla += digit
    entrada.delete(0,tkinter.END)
    entrada.insert(0,f"{valor_en_pantalla}")
    print(f"He fet click al boto {digit}")

def click_suma():
    global valor_en_pantalla
    global valor1
    global operacio
    operacio = "suma"
    valor1 = valor_en_pantalla
    entrada.delete(0,tkinter.END)
    entrada.insert(0,f"+")
    valor_en_pantalla =  0

def click_igual():
    global valor1  
    global valor_en_pantalla  
    print(f"El valor1 de click igual es {valor1}")
    entrada.delete(0,tkinter.END) 
    if operacio == "suma":
        valor_en_pantalla = valor1 +valor_en_pantalla
        entrada.insert(0,f"{valor_en_pantalla}")
    elif operacio == "resta":
        valor_en_pantalla = valor1 - valor_en_pantalla
        entrada.insert(0,f"{valor_en_pantalla}")
    elif operacio == "multiplicacio":
        valor_en_pantalla = valor1 * valor_en_pantalla
        entrada.insert(0,f"{valor_en_pantalla}")
    elif operacio == "divisio":
        valor_en_pantalla = valor1 / valor_en_pantalla
        entrada.insert(0,f"{valor_en_pantalla}")
        
def click_neteja():
    entrada.delete(0,tkinter.END)
    global valor1
    global valor_en_pantalla
    valor1 = 0
    valor_en_pantalla = 0
    entrada.insert(0,f"{valor_en_pantalla}")

def click_resta():
    global valor_en_pantalla
    global valor1
    global operacio
    operacio = "resta"
    valor1 = valor_en_pantalla
    entrada.delete(0,tkinter.END)
    entrada.insert(0,f"-")
    valor_en_pantalla =  0

def click_multiplicacio():
    global valor_en_pantalla
    global valor1
    global operacio
    operacio = "multiplicacio"
    valor1 = valor_en_pantalla
    entrada.delete(0,tkinter.END)
    entrada.insert(0,f"*")
    valor_en_pantalla =  0

def click_divisio():
    global valor_en_pantalla
    global valor1
    global operacio
    operacio = "divisio"
    valor1 = valor_en_pantalla
    entrada.delete(0,tkinter.END)
    entrada.insert(0,f"/")
    valor_en_pantalla =  0


finestra = tkinter.Tk()
entrada = tkinter.Entry(finestra,width=60)
entrada.grid(row=0, column=0, columnspan=3)
entrada.insert(0,"0")
finestra.title("Calculadora Unai")

boto_01 = tkinter.Button(finestra,text="1",padx=100, pady=20, fg="white", command=lambda : click_boto(1))
boto_02 = tkinter.Button(finestra,text="2",padx=100, pady=20, fg="white", command=lambda : click_boto(2))
boto_03 = tkinter.Button(finestra,text="3",padx=100, pady=20, fg="white", command=lambda : click_boto(3))
boto_04 = tkinter.Button(finestra,text="4",padx=100, pady=20, fg="white", command=lambda : click_boto(4))
boto_05 = tkinter.Button(finestra,text="5",padx=100, pady=20, fg="white", command=lambda : click_boto(5))
boto_06 = tkinter.Button(finestra,text="6",padx=100, pady=20, fg="white", command=lambda : click_boto(6))
boto_07 = tkinter.Button(finestra,text="7",padx=100, pady=20, fg="white", command=lambda : click_boto(7))
boto_08 = tkinter.Button(finestra,text="8",padx=100, pady=20, fg="white", command=lambda : click_boto(8))
boto_09 = tkinter.Button(finestra,text="9",padx=100, pady=20, fg="white", command=lambda : click_boto(9))
boto_00 = tkinter.Button(finestra,text="0",padx=100, pady=20, fg="white", command=lambda : click_boto(0))
boto_suma = tkinter.Button(finestra,text="+",padx=100, pady=20, fg="white", command=click_suma)
boto_igual = tkinter.Button(finestra,text="=",padx=100, pady=20, fg="white", command=click_igual)
boto_neteja = tkinter.Button(finestra,text="clr",padx=100, pady=20, fg="white", command=click_neteja)
boto_resta = tkinter.Button(finestra,text="-",padx=100, pady=20, fg="white", command=click_resta)
boto_multiplicacio = tkinter.Button(finestra,text="*",padx=100, pady=20, fg="white", command=click_multiplicacio)
boto_divisio = tkinter.Button(finestra,text="/",padx=100, pady=20, fg="white", command=click_divisio)

boto_01.grid(row=1, column=0)
boto_02.grid(row=1, column=1)
boto_03.grid(row=1, column=2)
boto_04.grid(row=2, column=0)
boto_05.grid(row=2, column=1)
boto_06.grid(row=2, column=2)
boto_07.grid(row=3, column=0)
boto_08.grid(row=3, column=1)
boto_09.grid(row=3, column=2)
boto_00.grid(row=4, column=0)
boto_suma.grid(row=4, column=1)
boto_multiplicacio.grid(row=4, column=2)
boto_neteja.grid(row=5, column=0)
boto_resta.grid(row=5, column=1)
boto_igual.grid(row=6, column=0)
boto_divisio.grid(row=5, column=2)

finestra.mainloop()
print("Hem tancat la finestra")

"""if __name__ == "__main__":
    main()"""