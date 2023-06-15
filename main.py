# Seshat - Administração Empresarial Profissionalizada
"""
É um programa facilitador com várias funções para o dia a dia de uma pequena empresa,
com vários facilitadores e recurso de edição de documentos a funções na empresa
"""
import tkinter
import customtkinter as ctk
from tkinter import ttk
import sqlite3

# Cria a apararencia inicial do programa.
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()


class Funcs:
    def limpa_tela(self):
        self.rsocial_empr.delete(0, tkinter.END)
        self.cnpj_empr.delete(0, tkinter.END)
        self.nfantasia.delete(0, tkinter.END)
        self.lagradouro.delete(0, tkinter.END)
        self.lagrad_numero.delete(0, tkinter.END)
        self.compl_end.delete(0, tkinter.END)
        self.cep_empr.delete(0, tkinter.END)
        self.telefone_emp.delete(0, tkinter.END)
        self.bairro_emp.delete(0, tkinter.END)
        self.cidade_emp.delete(0, tkinter.END)
        self.uf_emp.delete(0, tkinter.END)

    def conecta_bd(self): # Conecta ao banco de dados
        self.conn = sqlite3.connect("seshatbank.db")
        self.cursor = self.conn.cursor(), print("Conectando ao Banco...")
    def desconecta_bd(self): # Desconecta ao banco de dados
        self.conn.close(), print("Desconectado do banco")
    def montaTabelas(self):
        self.conecta_bd()
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS empresa (
            cod_empresa BIGINT PRIMARY KEY,
            razao_social CHAR(65) NOT NULL,
            cnpj BIGINT(14) NOT NULL,
            nome_fantasia CHAR(45) NOT NULL,
            end_empresa CHAR(60),
            num_end INT(5),
            end_complemento CHAR(40),
            cep INT(8),
            telefone_empresa BIGINT(11),
            bairro CHAR(30),
            cidade CHAR(30),
            uf CHAR(3)
            );
        """)
        self.conn.commit(), print("Banco de dados Criado!!!")
        self.desconecta_bd()
    def add_empresa(self):
        self.rsocial_empr = self.rsocial_empr.get()
        self.cnpj_empr = self.cnpj_empr.get()
        self.nfantasia = self.nfantasia.get()
        self.lagradouro = self.lagradouro.get()
        self.lagrad_numero = self.lagrad_numero.get()
        self.compl_end = self.compl_end.get()
        self.cep_empr = self.cep_empr.get()
        self.telefone_emp = self.telefone_emp.get()
        self.bairro_emp = self.bairro_emp.get()
        self.cidade_emp = self.cidade_emp.get()
        self.uf_emp = self.uf_emp.get()



class Application(Funcs):
    def __init__(self):
        self.root = root
        self.telaprincipal()
        self.frames_de_tela()
        self.widget_frame()
        self.montaTabelas()
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
        self.limpar = ctk.CTkButton(self.tabview.tab('Empresa'),
                                    text='limpar', command=self.limpa_tela)
        self.limpar.place(relx=0.01, rely=0.16, relwidth=0.16, relheight=0.06)
        """ Entrada de cadastro 
                                """
        # Nome da empresa / Razão Social
        self.lb_rsocial = ctk.CTkLabel(self.tabview.tab('Empresa'), text='Razão Social')
        self.lb_rsocial.place(relx=0.2, rely=0.009)
        self.rsocial_empr = ctk.CTkEntry(self.tabview.tab('Empresa'))
        self.rsocial_empr.place(relx=0.2, rely=0.062, relwidth=0.78)

        # CNPJ da empresa
        self.lb_cnpj = ctk.CTkLabel(self.tabview.tab('Empresa'), text='CNPJ')
        self.lb_cnpj.place(relx=0.2, rely=0.130)
        self.cnpj_empr = ctk.CTkEntry(self.tabview.tab('Empresa'),
                                      placeholder_text='digite só números')
        self.cnpj_empr.place(relx=0.2, rely=0.183, relwidth=0.23)

        # Nome fantasia da empresa
        self.lb_nfantasia = ctk.CTkLabel(self.tabview.tab('Empresa'), text='Nome Fantasia')
        self.lb_nfantasia.place(relx=0.44, rely=0.130)
        self.nfantasia = ctk.CTkEntry(self.tabview.tab('Empresa'))
        self.nfantasia.place(relx=0.44, rely=0.183, relwidth=0.54)

        # lagradouro / endereço
        self.lb_lagradouro = ctk.CTkLabel(self.tabview.tab('Empresa'), text='Endereço')
        self.lb_lagradouro.place(relx=0.2, rely=0.251)
        self.lagradouro = ctk.CTkEntry(self.tabview.tab('Empresa'))
        self.lagradouro.place(relx=0.2, rely=0.304, relwidth=0.69)

        # Número do endereço
        self.lb_lagrad_numero = ctk.CTkLabel(self.tabview.tab('Empresa'), text='Número')
        self.lb_lagrad_numero.place(relx=0.9, rely=0.251)
        self.lagrad_numero = ctk.CTkEntry(self.tabview.tab('Empresa'))
        self.lagrad_numero.place(relx=0.9, rely=0.304, relwidth=0.08)

        # complemento de endereço
        self.lb_compl_end = ctk.CTkLabel(self.tabview.tab('Empresa'), text='Complemento de endereço')
        self.lb_compl_end.place(relx=0.2, rely=0.372)
        self.compl_end = ctk.CTkEntry(self.tabview.tab('Empresa'))
        self.compl_end.place(relx=0.2, rely=0.425, relwidth=0.46)

        # CEP
        self.lb_cep = ctk.CTkLabel(self.tabview.tab('Empresa'), text='CEP')
        self.lb_cep.place(relx=0.67, rely=0.372)
        self.cep_empr = ctk.CTkEntry(self.tabview.tab('Empresa'))
        self.cep_empr.place(relx=0.67, rely=0.425, relwidth=0.13)

        # telefone da empresa
        self.lb_telefone_emp = ctk.CTkLabel(self.tabview.tab('Empresa'), text='Telefone')
        self.lb_telefone_emp.place(relx=0.81, rely=0.372)
        self.telefone_emp = ctk.CTkEntry(self.tabview.tab('Empresa'))
        self.telefone_emp.place(relx=0.81, rely=0.425, relwidth=0.17)

        # Bairro da empresa
        self.lb_bairro_emp = ctk.CTkLabel(self.tabview.tab('Empresa'), text='Bairro')
        self.lb_bairro_emp.place(relx=0.2, rely=0.493)
        self.bairro_emp = ctk.CTkEntry(self.tabview.tab('Empresa'))
        self.bairro_emp.place(relx=0.2, rely=0.546, relwidth=0.34)

        # Cidade da empresa
        self.lb_cidade_emp = ctk.CTkLabel(self.tabview.tab('Empresa'), text='Cidade')
        self.lb_cidade_emp.place(relx=0.55, rely=0.493)
        self.cidade_emp = ctk.CTkEntry(self.tabview.tab('Empresa'))
        self.cidade_emp.place(relx=0.55, rely=0.546, relwidth=0.34)

        # Estado da empresa
        self.lb_uf_emp = ctk.CTkLabel(self.tabview.tab('Empresa'), text='UF')
        self.lb_uf_emp.place(relx=0.9, rely=0.493)
        self.uf_emp = ctk.CTkEntry(self.tabview.tab('Empresa'))
        self.uf_emp.place(relx=0.9, rely=0.546, relwidth=0.08)

        """ Entrada de dados de empresa
                                        """
        self.lb_empresa = ctk.CTkLabel(self.tabview.tab('Empresa'), text='Dados de empresa')
        self.lb_empresa.place(relx=0.1, rely=0.614)
        self.lista_empresa = ttk.Treeview(self.tabview.tab('Empresa'), )
        self.lista_empresa.place(relx=0.1, rely=0.662, relwidth=0.88)


        # Botões da aba 'Configurações'.


Application()
