from tkinter import *
import os
try:
    from pytube import YouTube
except ImportError:
    print("Biblioteca em falta")
    if(os.name == "nt"):
        os.system("pip3 install pytube")
    else:
        os.system("sudo pip3 install pytube")

#-----------------------------------
# GUI
root = Tk()

class videoDown(Frame):
    def __init__(self, parent):
        super().__init__()

        self.root = root
        self.root["bg"] = "#414146"
        
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
    resposta = StringVar()
    def processo_final(self):
        self.resposta.set("Download concluído!")
        
    texto = StringVar()
    def download(self):
        if(self.texto.get() == ""):
            self.resposta.set("Tens que usar url do vídeo que vais baixar!")
        else:
             YouTube(self.texto.get()).streams.first().download()
             processo_final()

    #-----------------------------------
    # widgets
    def widgets_tela(self):
        self.label_1 = Label(self.root,
                            text = "Cole o seu link aqui(Ctrl + V):",
                             font = "Verdana 12 bold",
                             background = "#414146",
                             fg = "#fff"
                             )
        self.campo = Entry(self.root,
                          width = 60,
                          textvariable = self.texto
                          )
        self.btn_1 = Button(self.root,
                            text = "Tranferir",
                            background = "#0f3861",
                            fg = "#fff",
                            width = 10,
                            height = 2,
                            command = lambda: self.download()
                            )
        self.progresso = Label(self.root,
                               textvariable = self.resposta,
                               background = "#414146",
                               fg = "red"
                               )#atualizará

        self.label_1.place(relx = 0.30, rely = 0.2)
        self.campo.place(relx = 0.15, rely = 0.3, relheight = 0.1)
        self.btn_1.place(relx = 0.69, rely = 0.45)
        self.progresso.place(relx = 0.15, rely = 0.45)

#-----------------------------------
# class
videoDown(root)
