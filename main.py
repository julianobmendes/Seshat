# Seshat - Administração Empresarial Profissionalizada
"""
É um programa facilitador com várias funções para o dia a dia de uma pequena empresa,
com vários facilitadores e recurso de edição de documentos a funções na empresa
"""
import tkinter
import customtkinter


root = customtkinter.CTk()

class Application():
    def __init__(self):
        self.root = root
        self.telaPrincipal()
        root.mainloop()
    def telaPrincipal():
        self.root.title("Seshat - Administração Empresarial Profissionalizada")
        self.root.configure(background='gray')
        self.root.geometry('640x480')
        self.root.resizable(True, True)
        self.root.maxsize(width= 1600, height= 1200)
    


Application()
