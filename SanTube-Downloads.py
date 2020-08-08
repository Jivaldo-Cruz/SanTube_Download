from tkinter import *
import os
try:
    from pytube import YouTube
except ImportError:
    print("Biblioteca em falta.")
    os.system("pip install pytube")

#-----------------------------------
# GUI
root = Tk()

class videoDown:
    def __init__(self):
        self.root = root
        self.largura = self.root.winfo_screenwidth()
        self.altura = self.root.winfo_screenheight()
        self.calc_largura = int(self.largura/2) - int(700/2)
        self.calc_altura = int(self.altura/2) - int(500/2)
        self.root.title("SanTude-Downloads")
        self.root.geometry(f"700x500+{self.calc_largura}+{self.calc_altura}")
        self.root.resizable(False, False)
        
        self.widgets_tela()
        
        self.root.mainloop()

    #-----------------------------------
    # lógico
    texto = StringVar()
    def download(self):
        YouTube(self.texto.get()).streams.first().download()

    #-----------------------------------
    # widgets
    def widgets_tela(self):
        self.label_1 = Label(self.root,
                            text = "Cole o seu link aqui(Ctrl + V):",
                             font = "Verdana 12 bold",
                             )
        self.campo = Entry(self.root,
                          width = 60,
                          textvariable = self.texto
                          )
        self.btn_1 = Button(self.root,
                            text = "Tranferir",
                            background = "#414146",
                            fg = "#fff",
                            width = 10,
                            height = 2,
                            command = lambda: self.download()
                            )
        self.progresso = Label(self.root)#atualizará

        self.label_1.place(relx = 0.35, rely = 0.2)
        self.campo.place(relx = 0.15, rely = 0.3, relheight = 0.1)
        self.btn_1.place(relx = 0.69, rely = 0.45)

#-----------------------------------
# class
videoDown()
