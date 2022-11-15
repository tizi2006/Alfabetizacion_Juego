import tkinter
from PIL import ImageTk, Image
import os
import random
from functools import partial
import time


class JuegoVocales:
    
    def __init__(self):
        self.vocales = ["A", "E", "I", "O", "U"]
        self.ventana = tkinter.Tk()
        self.ventana.resizable(height=False, width=False)
        self.ventana.config(bg="#7FFFD4")
        menubar = tkinter.Menu(self.ventana)

        menubar1 = tkinter.Menu(menubar, tearoff=0)
        menubar1.add_command(label="Ir a PaMa", command=self.donothing)
        menubar1.add_command(label="Ir a vocales", command=self.donothing)
        menubar1.add_command(label="Ayuda", command=self.donothing)
        menubar1.add_separator()
        menubar1.add_command(label="Exit", command=self.ventana.quit)
        menubar.add_cascade(label="Juegos", menu=menubar1)
        menubar.add_cascade(label="Juegos", menu=menubar1)
        self.ventana.config(menu=menubar)
        self.frame = tkinter.Frame(self.ventana)
        self.frame2 = tkinter.Frame(self.ventana)
        self.frame3 = tkinter.Frame(self.ventana)
        self.frame4 = tkinter.Frame(self.ventana)
        self.frame5 = tkinter.Frame(self.ventana)
        self.frame.grid(row=0, column=0)
        self.frame2.grid(row=0, column=0)
        self.frame3.grid(row=1, column=0)
        self.frame4.grid(row=2, column=0)
        self.frame5.grid(row=3, column=0)
        self.contenido1 = os.listdir('fotos/')
        self.rango = (len(self.contenido1))
        self.contenido = []
        self.puntos = 0
        self.pos = 0
        self.mezclar()
        self.foto = self.sortear()
        self.panel = tkinter.Label(self.frame4)
        self.panel.config(image=self.foto)
        self.panel.pack(side="bottom", fill="both", expand="yes")
        self.eaa = tkinter.Label(self.frame4, text= "ACERTADAS:"+str(self.puntos))
        self.eaa.pack()
        for i in range(5):
            self.boton_lista = []
            self.boton = tkinter.Button(self.frame5, command=partial(self.v2, i), text=self.vocales[i])
            self.boton_lista.append(self.boton)
            self.boton.grid(column=i, row=0)
        self.ventana.bind("<Key>", self.tecla)
        self.indice = ""

    def mezclar(self):
        for i in range(self.rango):
            elemento = random.randint(0, len(self.contenido1)-1)
            self.contenido.append(self.contenido1.pop(elemento))

    def iniciar(self):
        self.ventana.mainloop()

    def tecla(self, e):
        if e.char.upper() in self.vocales:
            self.indice = self.vocales.index(e.char.upper())
            self.v2(self.indice)

    def sortear(self):
        print("sortear")
        self.ima = Image.open('fotos/' + self.contenido[self.pos])
        self.img = ImageTk.PhotoImage(self.ima, master=self.ventana)
        self.pos += 1
        return self.img


    def v2(self, i):
        if self.vocales[i] == self.contenido[self.pos-1][0].upper():
            self.frame3.configure(background="green")
            self.puntos += 1
            self.eaa.config(background="green", text="ACERTADAS:"+str(self.puntos))
            self.foto = self.sortear()
            self.panel.config(image=self.foto)
            
        else:
            self.eaa.config(background="red", text="ACERTADAS:"+str(self.puntos))
            self.foto = self.sortear()
            self.panel.config(image=self.foto)
            
            
    def donothing(self):
        x = 0


if __name__ == "__main__":
    juego = JuegoVocales()
    juego.iniciar()