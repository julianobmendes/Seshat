# Seshat - Administração Empresarial Profissionalizada
"""
É um programa facilitador com várias funções para o dia a dia de uma pequena empresa,
com vários facilitadores e recurso de edição de documentos a funções na empresa
"""
import customtkinter as ctk

# Cria a apararencia inicial do programa.
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()


class Application:
    def __init__(self):
        self.root = root
        self.telaprincipal()
        self.frames_de_tela()
        self.botoes()
        root.mainloop()

    def telaprincipal(self):
        self.root.title("Seshat - Administração Empresarial Profissionalizada")
        self.root.geometry('640x480')
        self.root.resizable(True, True)
        self.root.maxsize(width=1600, height=1200)
        self.root.minsize(width=640, height=480)

    def frames_de_tela(self):
        # self.frame_01 = ctk.CTkFrame(self.root)
        # self.frame_01.place(relx=0.02, rely=0.08, relwidth=0.96, relheight=0.91)
        self.tabview = ctk.CTkTabview(root, width=200)
        self.tabview.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        self.tabview.add('Aplicações')
        self.tabview.add('Nomes')
        self.tabview.add('Empresas')
        self.tabview.add('Configurações')
        self.tabview.tab('Aplicações').grid_columnconfigure(0, weight=1)
        self.tabview.tab('Nomes').grid_columnconfigure(0, weight=1)
        self.tabview.tab('Empresas').grid_columnconfigure(0, weight=1)
        self.tabview.tab('Configurações').grid_columnconfigure(0, weight=1)

    def botoes(self):
        # Botões da aba 'Aplicações'.
        self.bt_01 = ctk.CTkButton(self.tabview.tab('Aplicações'), text='nonono')
        self.bt_01.place(relx=0.01, rely=0.01, relwidth=0.12, relheight=0.06)
        self.bt_02 = ctk.CTkButton(self.tabview.tab('Aplicações'), text='nonono')
        self.bt_02.place(relx=0.01, rely=0.08, relwidth=0.12, relheight=0.06)
        # Botões da aba 'Nomes'.
        # Botões da aba 'Empresas'.
        self.bt_cadastrar = ctk.CTkButton(self.tabview.tab('Empresas'), text='Cadastrar')
        self.bt_cadastrar.place(relx=0.01, rely=0.01, relwidth=0.12, relheight=0.06)
        self.bt_03 = ctk.CTkButton(self.tabview.tab('Empresas'), text='nonono')
        self.bt_03.place(relx=0.01, rely=0.08, relwidth=0.12, relheight=0.06)
        # Botões da aba 'Configurações'.


Application()
