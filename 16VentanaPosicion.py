from tkinter import *


def pulsar():
    valor = int(entrada.get())
    valor = valor*10
    valor = ("Numero = " + str(valor))
    etiqueta.config(text=valor)


ventana = Tk()
ventana.title("Mi aplicacion")
miFrame = Frame(ventana)
miFrame.grid(column=0, row=0, padx=(50, 50), pady=(10, 10))
miFrame.columnconfigure(0, weight=1)
miFrame.rowconfigure(0, weight=1)
# Insertamos componentes
etiqueta = Label(miFrame, text='Numero')
etiqueta.grid(column=1, row=2, sticky=(W, E))
boton = Button(miFrame, text='Pulsame', command=pulsar)
boton.grid(column=2, row=3)
numero = ''
entrada = Entry(miFrame, width=15, textvariable=numero)
entrada.grid(column=2, row=2)
ventana.mainloop()
