import tkinter
valor_en_pantalla = 0
def click_boto_digit(digit):
    global valor_en_pantalla
    valor_en_pantalla *= 10
    valor_en_pantalla +=  digit

    entrada.delete(0, tkinter.END)
    entrada.insert(0, f"{valor_en_pantalla}")
    print(f"He fet click al boto  {digit} !!!")


finestra = tkinter.Tk()

entrada = tkinter.Entry(finestra, width=50)
entrada.grid(row=0,column=0, columnspan=4)
entrada.insert(0, "0")

boto_01 = tkinter.Button(finestra, 
                    text="1", 
                    padx=50, 
                    pady=50,
                    command=lambda : click_boto_digit(1))
boto_02 = tkinter.Button(finestra, 
                    text="2", 
                    padx=50, 
                    pady=50,
                    command=lambda : click_boto_digit(2))
boto_03 = tkinter.Button(finestra, 
                    text="3", 
                    padx=50, 
                    pady=50,
                    command=lambda : click_boto_digit(3))

boto_04 = tkinter.Button(finestra, 
                    text="4", 
                    padx=50, 
                    pady=50,
                    command=lambda : click_boto_digit(4))
boto_05 = tkinter.Button(finestra, 
                    text="5", 
                    padx=50, 
                    pady=50,
                    command=lambda : click_boto_digit(5))
boto_06 = tkinter.Button(finestra, 
                    text="6", 
                    padx=50, 
                    pady=50,
                    command=lambda : click_boto_digit(6))                    
boto_01.grid(row=1, column=0)
boto_02.grid(row=1, column=1)
boto_03.grid(row=1, column=2)

boto_04.grid(row=2, column=0)
boto_05.grid(row=2, column=1)
boto_06.grid(row=2, column=2)



finestra.mainloop()