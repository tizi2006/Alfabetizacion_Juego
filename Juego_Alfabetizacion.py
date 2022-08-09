import tkinter
from PIL import ImageTk, Image
import os
import random
from functools import partial
import time
from itertools import cycle
from tkinter import messagebox
from pynput.keyboard import Key, Listener
from tkinter import ttk


ventana1 = tkinter.Tk()
ventana1.title("Dificultad")
ventana1.geometry('250x150')
ls_des = ttk.Combobox(ventana1,width=17)
ls_des.place(x=30,y=77)
opciones = ["Vocales","Pa,Pe,Pi,Po,Pu","Ma,Me,Mi,Mo,Mu"]
ls_des['values']=opciones

def iniciar():
    iniciarJuego(ls_des.get())

boton2 = ttk.Button(text="Jugar",command=iniciar)
boton2.place(x=70, y=100)
    
def iniciarJuego(nivel):
    niveles = {
        'Vocales',
        'Pa,Pe,Pi,Po,Pu',
        'Ma,Me,Mi,Mo,Mu'
        }















vocales = ["A","E","I","O","U"]
ventana = tkinter.Tk()
ventana.resizable(height = 0, width = 0)
 
def tecla(e):
    if(e.char.upper() in vocales):
        indice = vocales.index(e.char.upper())
        v2(indice)

ventana.bind("<Key>", tecla)



frame = tkinter.Frame(ventana)
frame2 = tkinter.Frame(ventana)
frame3 = tkinter.Frame(ventana)
frame4 = tkinter.Frame(ventana)
frame.grid(row=0, column=0)
frame2.grid(row=1, column=0)
frame3.grid(row=0, column=0)
frame4.grid(row=2, column=0)



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
    panel.config(image=img)


panel = tkinter.Label(frame2)
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

eaa = tkinter.Label(frame3, text= "ACERTADAS:"+str(puntos))
eaa.pack()

def v2(i):
    global puntos
    if vocales[i] == contenido[pos-1][0].upper():
        frame3.configure(background="green")
        puntos+=1
        eaa.config(background="green", text= "ACERTADAS:"+str(puntos))
        sortear(panel)
        
    else:
        eaa.config(background="red", text= "ACERTADAS:"+str(puntos))
        sortear(panel)



for i in range(5):
    boton_lista=[]
    boton = tkinter.Button(frame4,command=partial(v2, i),text=vocales[i])
    boton_lista.append(boton)
    
    boton.grid(column=i,row=0)
    



    


ventana.mainloop()