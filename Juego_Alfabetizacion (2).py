import tkinter
from PIL import ImageTk, Image
import os
import random
from functools import partial

vocales = ["A","E","I","O","U"]
ventana = tkinter.Tk()
ventana.resizable(height = 0, width = 0)

frame = tkinter.Frame(ventana)
frame2 = tkinter.Frame(ventana)  
frame.grid(row=0, column=0)
frame2.grid(row=1, column=0)

contenido = os.listdir('/home/alcal-8-5/Documentos/VERTHI/ninos/fotos/')
print(contenido)


def recargar(panel):
    panel.destroy()
    panel = tkinter.Label(frame)
    foto = sortear(panel)
    panel.config(image=foto)

def sortear(panel):
    fotorandom = random.choice(contenido)
    foto = ImageTk.PhotoImage(Image.open('fotos/'+fotorandom))
    panel.config(image=foto)
    return foto



panel = tkinter.Label(frame)
foto = sortear(panel)
panel.config(image=foto)

panel.pack(side = "bottom", fill = "both", expand = "yes")


for i in range(5):
    boton1 = tkinter.Button(frame2,text=vocales[i], command=partial(recargar,panel))   
    boton1.grid(column=i,row=0)

ventana.mainloop()