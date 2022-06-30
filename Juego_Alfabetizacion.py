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

contenido1 = os.listdir('fotos/')
rango=(len(contenido1))
contenido= []
puntos = 0
for i in range (rango):
    elemento = random.randint(0, len(contenido1)-1)
    contenido.append(contenido1.pop(elemento))

pos = 0
photos = cycle(ImageTk.PhotoImage(Image.open('fotos/'+image)) for image in contenido)

def sortear(panel):
    global pos
    img = next(photos)
    pos+=1
    #fotorandom = random.choice(contenido)
    #print(fotorandom)
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


def v2(i):
    global puntos
    if vocales[i] == contenido[pos-1][0].upper():
        puntos+=1
        tkinter.messagebox.showinfo("JUEGO",f"GANASTE {puntos}")
        sortear(panel)
        
    else:
        tkinter.messagebox.showinfo("JUEGO","PERDISTE")
        sortear(panel)



for i in range(5):
    boton_lista=[]
    boton = tkinter.Button(frame2,command=partial(v2, i),text=vocales[i])
    boton_lista.append(boton)
    boton.grid(column=i,row=0)
    



    




ventana.mainloop()