import tkinter
from PIL import ImageTk, Image
import os


vocales = ["A","E","I","O","U"]
ventana = tkinter.Tk()
ventana.resizable(height = 0, width = 0)

frame = tkinter.Frame(ventana)
frame2 = tkinter.Frame(ventana)  
frame.grid(row=0, column=0)
frame2.grid(row=1, column=0)

foto = ImageTk.PhotoImage(Image.open("/home/alcal-8-5/Documentos/VERTHI/ninos/aguila.jpeg")) 

panel = tkinter.Label(frame, image = foto)
panel.pack(side = "bottom", fill = "both", expand = "yes")


for i in range(5):
    boton1 = tkinter.Button(frame2,text=vocales[i])   
    boton1.grid(column=i,row=0)
    
    
    

    
    
  
ventana.mainloop()