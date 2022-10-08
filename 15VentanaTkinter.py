from tkinter import *

ventana = Tk()
ventana.title("Aplicacion grafica Python")
etiqueta=Label(ventana,text='Etiqueta 01')
boton = Button(ventana, text='Pulsame')
etiqueta.pack()
boton.pack()
ventana.mainloop()