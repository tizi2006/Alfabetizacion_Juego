import tkinter
from PIL import ImageTk, Image
import os
import random
from functools import partial
import time
from vocales import JuegoVocales


class JuegoPaMa:
    
    def __init__(self):
        self.consonantes= ["P", "M"]
        self.vocales = ["A", "E", "I", "O", "U"]
        self.lista_btn_cons = []
        self.lista_btn_vocales = []
        self.cons = ""
        self.resp = ""
        self.ima = None
        self.img = None
        self.ventana = tkinter.Tk()
        self.ventana.resizable(height=False, width=False)
        menubar = tkinter.Menu(self.ventana)

        menubar1 = tkinter.Menu(menubar, tearoff=0)
        menubar1.add_command(label="Ir a PaMa", command=self.cambiarapama)
        menubar1.add_command(label="Ir a vocales", command=self.cambiaravocales)
        menubar1.add_command(label="Ayuda", command=self.donothing)
        menubar1.add_separator()
        menubar1.add_command(label="Exit", command=self.ventana.destroy)
        menubar.add_cascade(label="Juegos", menu=menubar1)
        self.ventana.config(menu=menubar)
        self.frame = tkinter.Frame(self.ventana)
        self.frame2 = tkinter.Frame(self.ventana)
        self.frame3 = tkinter.Frame(self.ventana)
        self.frame4 = tkinter.Frame(self.ventana)
        self.frame.grid(row=0, column=0)
        self.frame2.grid(row=1, column=0)
        self.frame3.grid(row=0, column=0)
        self.frame4.grid(row=2, column=0)
        self.frame5 = tkinter.Frame(self.frame4, height=30,width=87.5)
        self.frame52 = tkinter.Frame(self.frame4, height=30,width=87.5)
        self.frames = [self.frame5, self.frame52]
        self.frame6 = tkinter.Frame(self.frame4, height=175)
        self.frame5.grid_propagate(0)
        self.frame5.grid(row=0, column=0)
        self.frame52.grid_propagate(0)
        self.frame52.grid(row=0, column=1)
        self.frame6.grid(row=0, column=2)
        self.contenido1 = os.listdir('PPP/')
        self.rango = (len(self.contenido1))
        self.contenido = []
        self.puntos = 0
        self.pos = 0
        self.mezclar()
        self.foto = self.sortear()
        self.panel = tkinter.Label(self.frame2)
        self.panel.config(image=self.foto)
        self.panel.pack(side="bottom", fill="both", expand="yes")
        self.eaa = tkinter.Label(self.frame3, text= "ACERTADAS:"+str(self.puntos))
        self.eaa.pack()
        for i in range(2):
            ubi = ["W","E"]
            self.boton = tkinter.Button(self.frames[i], command=partial(self.press_cons, i), text=self.consonantes[i])
            self.lista_btn_cons.append(self.boton)
            self.boton.grid(column=i, row=0, sticky=ubi[i])
        self.frame5.grid_columnconfigure(0, weight=0)
        self.frame52.grid_columnconfigure(0, weight=0)
        for i in range(5):
            self.boton = tkinter.Button(self.frame6, command=partial(self.press_vocal, i), text=self.vocales[i])
            self.lista_btn_vocales.append(self.boton)
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
        print(e)
        if e.char.upper() in self.vocales:
            self.indice = self.vocales.index(e.char.upper())
            self.press_vocal(self.indice)
        elif e.char.upper() in self.consonantes:
            self.indice = self.consonantes.index(e.char.upper())
            self.press_cons(self.indice)

    def sortear(self):
        self.ima = Image.open('PPP/' + self.contenido[self.pos])
        self.img = ImageTk.PhotoImage(self.ima, master=self.ventana)
        self.pos += 1
        return self.img

    def press_cons(self, i):
        print(i)
        self.lista_btn_cons[i-1].config(relief=tkinter.RAISED)
        self.lista_btn_cons[i].config(relief=tkinter.SUNKEN)
        self.cons = self.lista_btn_cons[i].cget("text")
        
    def press_vocal(self, i):
        print(i)
        if self.cons:
            self.resp = self.cons + self.lista_btn_vocales[i].cget("text")
            if self.resp.upper() == self.contenido[self.pos-1][0:2].upper():
                self.frame3.configure(background="green")
                self.puntos += 1
                self.eaa.config(background="green", text="ACERTADAS:" + str(self.puntos))
            else:
                self.eaa.config(background="red", text="ACERTADAS:" + str(self.puntos))
            self.foto = self.sortear()
            self.panel.config(image=self.foto)
            self.lista_btn_cons[0].config(relief=tkinter.RAISED)
            self.lista_btn_cons[1].config(relief=tkinter.RAISED)



    def cambiarapama(self):
        juego = JuegoPaMa()
        juego.iniciar()
        self.ventana.quit

    def cambiaravocales(self):
        juego = JuegoVocales()
        juego.iniciar()
        self.ventana.destroy
        
        
        
    def donothing(self):
        x = 0




if __name__ == "__main__":
    juego = JuegoPaMa()
    juego.iniciar()
