# Seshat - Administração Empresarial Profissionalizada
"""
É um programa facilitador com várias funções para o dia a dia de uma pequena empresa,
com vários facilitadores e recurso de edição de documentos a funções na empresa
"""
import tkinter
import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()


class Application:
    def __init__(self):
        self.root = root
        self.telaPrincipal()
        self.frames_de_tela()
        root.mainloop()

    def telaPrincipal(self):
        self.root.title("Seshat - Administração Empresarial Profissionalizada")
        self.root.geometry('640x480')
        self.root.resizable(True, True)
        self.root.maxsize(width=1600, height=1200)
        self.root.minsize(width=640, height=480)
    def frames_de_tela(self):
        self.frame_01 = customtkinter.CTkFrame(self.root)
        self.frame_01.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)



Application()
