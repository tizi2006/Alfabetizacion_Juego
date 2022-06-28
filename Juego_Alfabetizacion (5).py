import tkinter
from PIL import ImageTk, Image
import os
import random
from functools import partial
import time
from itertools import cycle
from tkinter import messagebox

vocales = ["A","E","I","O","U"]
ventana = tkinter.Tk()
ventana.resizable(height = 0, width = 0)

frame = tkinter.Frame(ventana)
frame2 = tkinter.Frame(ventana)
frame3 = tkinter.Frame(ventana)
frame.grid(row=0, column=0)
frame2.grid(row=1, column=0)
frame3.grid(row=0, column=0)

contenido = os.listdir('/home/alcal-8-5/Documentos/VERTHI/Alfabetizacion_Juego/fotos/')
print(contenido)

photos = cycle(ImageTk.PhotoImage(Image.open('fotos/'+image)) for image in contenido)

def sortear(panel):
    img = next(photos)
    fotorandom = random.choice(contenido)
    #foto = ImageTk.PhotoImage(Image.open('fotos/'+fotorandom))
    panel.config(image=img)


panel = tkinter.Label(frame)
foto = sortear(panel)
panel.config(image=foto)

panel.pack(side = "bottom", fill = "both", expand = "yes")

def recargar(panel):
    panel.destroy()
    intermedia()
    
def intermedia():
    time.sleep(0.5)
    frame = tkinter.Frame(ventana)
    frame.grid(row=0, column=0)
    panel = tkinter.Label(frame)
    sortear(panel)


def v2():
    Ventana4=Toplevel()
    Ventana4.geometry("200x200")
    



for i in range(5):
    boton1 = tkinter.Button(frame2,command=partial(v2),text=vocales[i])   
    boton1.grid(column=i,row=0)
    



    
    
    
boton2 = tkinter.Button(text="siguiente",command=partial(sortear,panel))
boton2.grid(column=6,row=1)



ventana.mainloop()