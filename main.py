# Seshat - Administração Empresarial Profissionalizada
"""
É um programa facilitador com várias funções para o dia a dia de uma pequena empresa,
com vários facilitadores e recurso de edição de documentos a funções na empresa
"""
import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()


class Application:
    def __init__(self):
        self.root = root
        self.telaprincipal()
        self.frames_de_tela()
        root.mainloop()

    def telaprincipal(self):
        self.root.title("Seshat - Administração Empresarial Profissionalizada")
        self.root.geometry('640x480')
        self.root.resizable(True, True)
        self.root.maxsize(width=1600, height=1200)
        self.root.minsize(width=640, height=480)
    def frames_de_tela(self):
        self.tabview = ctk.CTkTabview(root, width=200)
        self.tabview.pack()
        self.tabview.add('Aplicações')
        self.tabview.add('Nomes')
        self.tabview.add('Empresas')
        self.tabview.add('Configurações')
        self.tabview.tab('Aplicações').grid_columnconfigure(0, weight=1)
        self.tabview.tab('Nomes').grid_columnconfigure(0, weight=1)
        self.tabview.tab('Empresas').grid_columnconfigure(0, weight=1)
        self.tabview.tab('Configurações').grid_columnconfigure(0, weight=1)
        self.frame_01 = ctk.CTkFrame(self.root)
        self.frame_01.place(relx=0.02, rely=0.08, relwidth=0.96, relheight=0.91)


Application()
