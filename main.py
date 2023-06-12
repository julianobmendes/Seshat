# Seshat - Administração Empresarial Profissionalizada
"""
É um programa facilitador com várias funções para o dia a dia de uma pequena empresa,
com vários facilitadores e recurso de edição de documentos a funções na empresa
"""
import customtkinter as ctk
from tkinter import ttk

# Cria a apararencia inicial do programa.
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()


class Application:
    def __init__(self):
        self.root = root
        self.telaprincipal()
        self.frames_de_tela()
        self.widget_frame()
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
        self.tabview.add('Empresa')
        self.tabview.add('Configurações')
        self.tabview.tab('Aplicações').grid_columnconfigure(0, weight=1)
        self.tabview.tab('Nomes').grid_columnconfigure(0, weight=1)
        self.tabview.tab('Empresa').grid_columnconfigure(0, weight=1)
        self.tabview.tab('Configurações').grid_columnconfigure(0, weight=1)

    def widget_frame(self):
        # Aba 'Aplicações'.
        """ botões
                    """
        self.bt_01 = ctk.CTkButton(self.tabview.tab('Aplicações'), text='nonono')
        self.bt_01.place(relx=0.01, rely=0.01, relwidth=0.12, relheight=0.06)
        self.bt_02 = ctk.CTkButton(self.tabview.tab('Aplicações'), text='nonono')
        self.bt_02.place(relx=0.01, rely=0.08, relwidth=0.12, relheight=0.06)
        # Botões da aba 'Nomes'.

        # Aba 'Empresa'.
        """ botões
                    """
        self.bt_cadastrar = ctk.CTkButton(self.tabview.tab('Empresa'),
                                          text='Cadastrar')
        self.bt_cadastrar.place(relx=0.01, rely=0.08, relwidth=0.16, relheight=0.06)
        self.limpar = ctk.CTkButton(self.tabview.tab('Empresa'), text='limpar')
        self.limpar.place(relx=0.01, rely=0.16, relwidth=0.16, relheight=0.06)
        """ Entrada de cadastro 
                                """
        # Nome da empresa / Razão Social
        self.lb_rsocial = ctk.CTkLabel(self.tabview.tab('Empresa'), text='Razão Social')
        self.lb_rsocial.place(relx=0.2, rely=0.009)
        self.rsocial_empr = ctk.CTkEntry(self.tabview.tab('Empresa'))
        self.rsocial_empr.place(relx=0.2, rely=0.07, relwidth=0.78)

        # CNPJ da empresa
        self.lb_cnpj = ctk.CTkLabel(self.tabview.tab('Empresa'), text='CNPJ')
        self.lb_cnpj.place(relx=0.2, rely=0.14)
        self.cnpj_empr = ctk.CTkEntry(self.tabview.tab('Empresa'),
                                      placeholder_text='digite só números')
        self.cnpj_empr.place(relx=0.2, rely=0.201, relwidth=0.23)

        # Nome fantasia da empresa
        self.lb_nfantasia = ctk.CTkLabel(self.tabview.tab('Empresa'), text='Nome Fantasia')
        self.lb_nfantasia.place(relx=0.44, rely=0.14)
        self.nfantasia = ctk.CTkEntry(self.tabview.tab('Empresa'))
        self.nfantasia.place(relx=0.44, rely=0.201, relwidth=0.54)

        # CEP
        self.lb_cep = ctk.CTkLabel(self.tabview.tab('Empresa'), text='CEP')
        self.lb_cep.place(relx=0.2, rely=0.272)
        self.cep_empr = ctk.CTkEntry(self.tabview.tab('Empresa'))
        self.cep_empr.place(relx=0.2, rely=0.333, relwidth=0.13)

        # lagradouro / endereço
        self.lb_lagradouro = ctk.CTkLabel(self.tabview.tab('Empresa'), text='Endereço')
        self.lb_lagradouro.place(relx=0.34, rely=0.272)
        self.lagradouro = ctk.CTkEntry(self.tabview.tab('Empresa'))
        self.lagradouro.place(relx=0.34, rely=0.333, relwidth=0.55)

        # Número do endereço
        self.lb_lagrad_numero = ctk.CTkLabel(self.tabview.tab('Empresa'), text='Número')
        self.lb_lagrad_numero.place(relx=0.9, rely=0.272)
        self.lagrad_numero = ctk.CTkEntry(self.tabview.tab('Empresa'))
        self.lagrad_numero.place(relx=0.9, rely=0.333, relwidth=0.08)

        # telefone da empresa
        self.lb_telefone_emp = ctk.CTkLabel(self.tabview.tab('Empresa'), text='Telefone')
        self.lb_telefone_emp.place(relx=0.2, rely=0.405)
        self.telefone_emp = ctk.CTkEntry(self.tabview.tab('Empresa'))
        self.telefone_emp.place(relx=0.2, rely=0.477, relwidth=0.17)

        # Bairro da empresa
        self.lb_bairro_emp = ctk.CTkLabel(self.tabview.tab('Empresa'), text='Bairro')
        self.lb_bairro_emp.place(relx=0.38, rely=0.405)
        self.bairro_emp = ctk.CTkEntry(self.tabview.tab('Empresa'))
        self.bairro_emp.place(relx=0.38, rely=0.477, relwidth=0.24)

        # Cidade da empresa
        self.lb_cidade_emp = ctk.CTkLabel(self.tabview.tab('Empresa'), text='Cidade')
        self.lb_cidade_emp.place(relx=0.63, rely=0.405)
        self.cidade_emp = ctk.CTkEntry(self.tabview.tab('Empresa'))
        self.cidade_emp.place(relx=0.63, rely=0.477, relwidth=0.26)

        # Estado da empresa
        self.lb_uf_emp = ctk.CTkLabel(self.tabview.tab('Empresa'), text='UF')
        self.lb_uf_emp.place(relx=0.9, rely=0.405)
        self.uf_emp = ctk.CTkEntry(self.tabview.tab('Empresa'))
        self.uf_emp.place(relx=0.9, rely=0.477, relwidth=0.08)

        """ Entrada de dados de empresa
                                        """
        self.lb_empresa = ctk.CTkLabel(self.tabview.tab('Empresa'), text='Dados de empresa')
        self.lb_empresa.place(relx=0.1, rely=0.58)
        self.lista_empresa = ttk.Treeview(self.tabview.tab('Empresa'), )
        self.lista_empresa.place(relx=0.1, rely=0.65, relwidth=0.88)


        # Botões da aba 'Configurações'.


Application()
