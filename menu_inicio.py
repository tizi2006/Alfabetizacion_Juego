import tkinter
from tkinter import ttk
from vocales import JuegoVocales
import os

class Juego:

    def __init__(self):
        self.ventana1 = tkinter.Tk()
        self.ventana1.title("Dificultad")
        self.ventana1.geometry('250x150')
        self.ls_des = ttk.Combobox(self.ventana1,width=17)
        self.ls_des.place(x=30,y=77)
        self.opciones = ["Vocales","Pa,Pe,Pi,Po,Pu","Ma,Me,Mi,Mo,Mu"]
        self.ls_des['values']=self.opciones
        self.boton2 = ttk.Button(text="Jugar", command=self.iniciar)
        self.boton2.place(x=70, y=100)
        self.nivel = ""
        self.juego = ""
        self.niveles = {
            'Vocales': JuegoVocales,
            'Pa,Pe,Pi,Po,Pu': 10,
            'Ma,Me,Mi,Mo,Mu': 10
        }
        self.ventana1.mainloop()

    def iniciar(self):
        self.nivel = self.ls_des.get()
        self.iniciarjuego()

    def iniciarjuego(self):
        self.juego = self.niveles[self.nivel]()
        self.juego.contenido1 = os.listdir('fotos/')
        self.juego.iniciarjuego()


if __name__ == "__main__":
    juego = Juego()


