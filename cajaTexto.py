import tkinter
from tkinter import ttk



class Application(ttk.Frame):
    def __init__(self, main_window, texto):
        super().__init__(main_window)
        main_window.geometry("400x500")
        self.text = tkinter.StringVar(value=texto)

        self.label = tkinter.Label(self)
        self.label.grid(column=0, row=0, pady=10, padx=10, sticky="e")
        self.label2 = tkinter.Label(self, textvariable=self.text)
        self.grid_columnconfigure(1, weight=1)
        self.label2.grid(column=1, row=0, pady=20, padx=10,  sticky="nswe")
        self.label2.bind( "<Configure>", self.on_label_resize)

        
    def on_label_resize(self,  event):
        event.widget["wraplength"] = event.width


if __name__ == "__main__":
    root = tkinter.Tk()
    texto = ("Esto es un texto largo de ejemplo "
                                        "para Stackoverflow."
                                        "Esto es un texto largo de ejemplo "
                                        "para Stackoverflow.")
    app = Application(root, texto)
    app.pack(expand=True, fill='both')
    root.mainloop()