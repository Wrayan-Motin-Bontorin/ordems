from datetime import datetime
from tkinter import *
from tkinter import ttk
import sqlite3

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser


root = Tk()
cor1 = "#1a2238"  # background
cor2 = "#5b7fe3"  # borda
cor3 = "#dfe3ee"  # background frame
cor4 = "#6b8ce8"  # cor do botao


class Relatorios():
    def PrintPDF(self):
        webbrowser.open(f'Ordem {self.en_ordem.get()}.pdf')

    def Gerar_relatorio(self):
        self.c = canvas.Canvas(f"Ordem {self.en_ordem.get()}.pdf")
        self.ordemRel = self.en_ordem.get()
        self.placaRel = self.en_placa.get()
        self.cod1Rel = self.en_cod1.get()
        self.prod1Rel = self.en_prod1.get()
        self.qtd1Rel = self.en_qtd1.get()
        self.acond1Rel = self.en_acond1.get()
        self.cod2Rel = self.en_cod2.get()
        self.prod2Rel = self.en_prod2.get()
        self.qtd2Rel = self.en_qtd2.get()
        self.acond2Rel = self.en_acond2.get()
        self.cod3Rel = self.en_cod3.get()
        self.prod3Rel = self.en_prod3.get()
        self.qtd3Rel = self.en_qtd3.get()
        self.acond3Rel = self.en_acond3.get()
        self.cod4Rel = self.en_cod4.get()
        self.prod4Rel = self.en_prod4.get()
        self.qtd4Rel = self.en_qtd4.get()
        self.acond4Rel = self.en_acond4.get()
        self.cod5Rel = self.en_cod5.get()
        self.prod5Rel = self.en_prod5.get()
        self.qtd5Rel = self.en_qtd5.get()
        self.acond5Rel = self.en_acond5.get()
        self.cod6Rel = self.en_cod6.get()
        self.prod6Rel = self.en_prod6.get()
        self.qtd6Rel = self.en_qtd6.get()
        self.acond6Rel = self.en_acond6.get()
        self.cod7Rel = self.en_cod7.get()
        self.prod7Rel = self.en_prod7.get()
        self.qtd7Rel = self.en_qtd7.get()
        self.acond7Rel = self.en_acond7.get()
        self.cod8Rel = self.en_cod8.get()
        self.prod8Rel = self.en_prod8.get()
        self.qtd8Rel = self.en_qtd8.get()
        self.acond8Rel = self.en_acond8.get()
        self.dataRel = self.en_data.get()

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(200, 790, 'Ordem de Carregamento')

        self.c.setFont("Helvetica-Bold", 20)
        self.c.drawString(100, 740, "PLACA: " + self.placaRel)

        self.c.setFont("Helvetica-Bold", 12)
        self.c.drawString(440, 730, 'ORDEM: ' + self.ordemRel)
        self.c.drawString(440, 750, 'DATA: ' + self.dataRel)
        self.c.drawString(40, 700, "CODIGO")
        self.c.drawString(180, 700, "DESCRIÇÃO")
        self.c.drawString(350, 700, "QTDE")
        self.c.drawString(450, 700, "ACONDICIONAMENTO")
        # codigo
        self.c.drawString(60, 680, "" + self.cod1Rel)
        self.c.drawString(60, 665, "" + self.cod2Rel)
        self.c.drawString(60, 650, "" + self.cod3Rel)
        self.c.drawString(60, 635, "" + self.cod4Rel)
        self.c.drawString(60, 620, "" + self.cod5Rel)
        self.c.drawString(60, 605, "" + self.cod6Rel)
        self.c.drawString(60, 590, "" + self.cod7Rel)
        self.c.drawString(60, 575, "" + self.cod8Rel)
        # produto
        self.c.drawString(210, 680, "" + self.prod1Rel)
        self.c.drawString(210, 665, "" + self.prod2Rel)
        self.c.drawString(210, 650, "" + self.prod3Rel)
        self.c.drawString(210, 635, "" + self.prod4Rel)
        self.c.drawString(210, 620, "" + self.prod5Rel)
        self.c.drawString(210, 605, "" + self.prod6Rel)
        self.c.drawString(210, 590, "" + self.prod7Rel)
        self.c.drawString(210, 575, "" + self.prod8Rel)
        # quantidade
        self.c.drawString(365, 680, "" + self.qtd1Rel)
        self.c.drawString(365, 665, "" + self.qtd2Rel)
        self.c.drawString(365, 650, "" + self.qtd3Rel)
        self.c.drawString(365, 635, "" + self.qtd4Rel)
        self.c.drawString(365, 620, "" + self.qtd5Rel)
        self.c.drawString(365, 605, "" + self.qtd6Rel)
        self.c.drawString(365, 590, "" + self.qtd7Rel)
        self.c.drawString(365, 575, "" + self.qtd8Rel)
        # acondicionamento
        self.c.drawString(480, 680, "" + self.acond1Rel)
        self.c.drawString(480, 665, "" + self.acond2Rel)
        self.c.drawString(480, 650, "" + self.acond3Rel)
        self.c.drawString(480, 635, "" + self.acond4Rel)
        self.c.drawString(480, 620, "" + self.acond5Rel)
        self.c.drawString(480, 605, "" + self.acond6Rel)
        self.c.drawString(480, 590, "" + self.acond7Rel)
        self.c.drawString(480, 575, "" + self.acond8Rel)

        self.c.showPage()
        self.c.save()
        self.PrintPDF()


class Funcs():
    def Limpa_Tela(self):
        self.en_data.delete(0, END)
        self.en_ordem.delete(0, END)
        self.en_placa.delete(0, END)
        self.en_cod1.delete(0, END)
        self.en_prod1.delete(0, END)
        self.en_qtd1.delete(0, END)
        self.en_acond1.delete(0, END)
        self.en_cod2.delete(0, END)
        self.en_prod2.delete(0, END)
        self.en_qtd2.delete(0, END)
        self.en_acond2.delete(0, END)
        self.en_cod3.delete(0, END)
        self.en_prod3.delete(0, END)
        self.en_qtd3.delete(0, END)
        self.en_acond3.delete(0, END)
        self.en_cod4.delete(0, END)
        self.en_prod4.delete(0, END)
        self.en_qtd4.delete(0, END)
        self.en_acond4.delete(0, END)
        self.en_cod5.delete(0, END)
        self.en_prod5.delete(0, END)
        self.en_qtd5.delete(0, END)
        self.en_acond5.delete(0, END)
        self.en_cod6.delete(0, END)
        self.en_prod6.delete(0, END)
        self.en_qtd6.delete(0, END)
        self.en_acond6.delete(0, END)
        self.en_cod7.delete(0, END)
        self.en_prod7.delete(0, END)
        self.en_qtd7.delete(0, END)
        self.en_acond7.delete(0, END)
        self.en_cod8.delete(0, END)
        self.en_prod8.delete(0, END)
        self.en_qtd8.delete(0, END)
        self.en_acond8.delete(0, END)

    def conecta_db(self):
        self.conn = sqlite3.connect("ORDENS.bd")
        self.cursor = self.conn.cursor()

    def desconecta_db(self):
        self.conn.close()
        print("Banco de dados DESCONECTADO")

    def monta_tabelas(self):
        self.conecta_db()
        print("conectando ao banco de dados")
        # criando a tabela
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS ORDENS(
                ordem  INTEGER PRIMARY KEY,
                placa  CHAR(20) NOT NULL,
                cod1   CHAR(5),
                prod1  CHAR(40),
                qtd1   CHAR(20),
                acond1 CHAR(20),
                cod2   CHAR(5),
                prod2  CHAR(40),
                qtd2   CHAR(20),
                acond2 CHAR(20),
                cod3   CHAR(5),
                prod3  CHAR(40),
                qtd3   CHAR(20),
                acond3 CHAR(20),
                cod4   CHAR(5),
                prod4  CHAR(40),
                qtd4   CHAR(20),
                acond4 CHAR(20),
                cod5   CHAR(5),
                prod5  CHAR(40),
                qtd5   CHAR(20),
                acond5 CHAR(20),
                cod6   CHAR(5),
                prod6  CHAR(40),
                qtd6   CHAR(20),
                acond6 CHAR(20),
                cod7   CHAR(5),
                prod7  CHAR(40),
                qtd7   CHAR(20),
                acond7 CHAR(20),
                cod8   CHAR(5),
                prod8  CHAR(40),
                qtd8   CHAR(20),
                acond8 CHAR(20),
                data CHAR(12)
            );
        """)
        self.conn.commit()
        print("banco de cados criado")
        self.desconecta_db()

    def variaveis(self):
        self.ordem = self.en_ordem.get()
        self.placa = self.en_placa.get()
        self.cod1 = self.en_cod1.get()
        self.prod1 = self.en_prod1.get()
        self.qtd1 = self.en_qtd1.get()
        self.acond1 = self.en_acond1.get()
        self.cod2 = self.en_cod2.get()
        self.prod2 = self.en_prod2.get()
        self.qtd2 = self.en_qtd2.get()
        self.acond2 = self.en_acond2.get()
        self.cod3 = self.en_cod3.get()
        self.prod3 = self.en_prod3.get()
        self.qtd3 = self.en_qtd3.get()
        self.acond3 = self.en_acond3.get()
        self.cod4 = self.en_cod4.get()
        self.prod4 = self.en_prod4.get()
        self.qtd4 = self.en_qtd4.get()
        self.acond4 = self.en_acond4.get()
        self.cod5 = self.en_cod5.get()
        self.prod5 = self.en_prod5.get()
        self.qtd5 = self.en_qtd5.get()
        self.acond5 = self.en_acond5.get()
        self.cod6 = self.en_cod6.get()
        self.prod6 = self.en_prod6.get()
        self.qtd6 = self.en_qtd6.get()
        self.acond6 = self.en_acond6.get()
        self.cod7 = self.en_cod7.get()
        self.prod7 = self.en_prod7.get()
        self.qtd7 = self.en_qtd7.get()
        self.acond7 = self.en_acond7.get()
        self.cod8 = self.en_cod8.get()
        self.prod8 = self.en_prod8.get()
        self.qtd8 = self.en_qtd8.get()
        self.acond8 = self.en_acond8.get()
        self.data = self.en_data.get()

    def adicionar_ordem(self):
        self.variaveis()
        self.conecta_db()

        self.cursor.execute("""INSERT INTO ORDENS(placa, cod1, prod1, qtd1, acond1, cod2, prod2, qtd2, acond2, cod3, prod3, qtd3, acond3, cod4, prod4, qtd4, acond4, cod5, prod5, qtd5, acond5, cod6, prod6, qtd6, acond6, cod7, prod7, qtd7, acond7, cod8, prod8, qtd8, acond8, data)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (self.placa, self.cod1, self.prod1, self.qtd1, self.acond1, self.cod2, self.prod2, self.qtd2, self.acond2, self.cod3, self.prod3, self.qtd3, self.acond3, self.cod4, self.prod4, self.qtd4, self.acond4, self.cod5, self.prod5, self.qtd5, self.acond5, self.cod6, self.prod6, self.qtd6, self.acond6, self.cod7, self.prod7, self.qtd7, self.acond7, self.cod8, self.prod8, self.qtd8, self.acond8, self.data))
        self.conn.commit()
        self.desconecta_db()
        self.select_lista()
        self.Limpa_Tela()
        self.datahoje()

    def apaga_ordem(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute(
            """ DELETE FROM ORDENS WHERE ordem = ?""", [self.ordem])
        self.conn.commit()
        self.desconecta_db()
        self.Limpa_Tela()
        self.datahoje()
        self.select_lista()

    def alterar_ordem(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute(""" UPDATE ORDENS SET placa = ?, cod1 = ?, prod1 = ?, qtd1 = ?, acond1 = ?, cod2 = ?, prod2 = ?, qtd2 = ?, acond2 = ?, cod3 = ?, prod3 = ?, qtd3 = ?, acond3 = ?, cod4 = ?, prod4 = ?, qtd4 = ?, acond4 = ?, cod5 = ?, prod5 = ?, qtd5 = ?, acond5 = ?, cod6 = ?, prod6 = ?, qtd6 = ?, acond6 = ?, cod7 = ?, prod7 = ?, qtd7 = ?, acond7 = ?, cod8 = ?, prod8 = ?, qtd8 = ?, acond8 = ?, data = ?
        WHERE ordem = ?""", (self.placa, self.cod1, self.prod1, self.qtd1, self.acond1, self.cod2, self.prod2, self.qtd2, self.acond2, self.cod3, self.prod3, self.qtd3, self.acond3, self.cod4, self.prod4, self.qtd4, self.acond4, self.cod5, self.prod5, self.qtd5, self.acond5, self.cod6, self.prod6, self.qtd6, self.acond6, self.cod7, self.prod7, self.qtd7, self.acond7, self.cod8, self.prod8, self.qtd8, self.acond8, self.data, self.ordem))
        self.conn.commit()
        self.desconecta_db()
        self.select_lista()
        self.Limpa_Tela()

    def buscar_placa(self):
        self.conecta_db()
        self.Ordem_carregamento.delete(*self.Ordem_carregamento.get_children())

        self.en_placa.insert(END, "%")
        placa = self.en_placa.get()
        self.cursor.execute(
            """SELECT ordem, placa, cod1, prod1, qtd1, acond1, cod2, prod2, qtd2, acond2, cod3, prod3, qtd3, acond3, cod4, prod4, qtd4, acond4, cod5, prod5, qtd5, acond5, cod6, prod6, qtd6, acond6, cod7, prod7, qtd7, acond7, cod8, prod8, qtd8, acond8, data FROM ORDENS WHERE placa LIKE '%s'ORDER BY ordem DESC""" % placa)
        buscaplaca = self.cursor.fetchall()

        for i in buscaplaca:
            self.Ordem_carregamento.insert("", END, values=i)
        self.Limpa_Tela()
        self.desconecta_db()

    def select_lista(self):
        self.Ordem_carregamento.delete(*self.Ordem_carregamento.get_children())
        self.conecta_db()
        lista = self.cursor.execute(""" SELECT ordem, placa, cod1, prod1, qtd1, acond1, cod2, prod2, qtd2, acond2, cod3, prod3, qtd3, acond3, cod4, prod4, qtd4, acond4, cod5, prod5, qtd5, acond5, cod6, prod6, qtd6, acond6, cod7, prod7, qtd7, acond7, cod8, prod8, qtd8, acond8, data FROM ORDENS 
            ORDER BY ordem DESC; """)
        for i in lista:
            self.Ordem_carregamento.insert("", END, values=i)
        self.desconecta_db()

    def on_doubleclick(self, event):
        self.Limpa_Tela()
        self.Ordem_carregamento.selection()

        for n in self.Ordem_carregamento.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18, col19, col20, col21, col22, col23, col24, col25, col26, col27, col28, col29, col30, col31, col32, col33, col34, col35 = self.Ordem_carregamento.item(
                n, 'values')
            self.en_ordem.insert(END, col1)
            self.en_placa.insert(END, col2)
            self.en_cod1.insert(END,  col3)
            self.en_prod1.insert(END, col4)
            self.en_qtd1.insert(END, col5)
            self.en_acond1.insert(END, col6)
            self.en_cod2.insert(END, col7)
            self.en_prod2.insert(END, col8)
            self.en_qtd2.insert(END, col9)
            self.en_acond2.insert(END, col10)
            self.en_cod3.insert(END, col11)
            self.en_prod3.insert(END, col12)
            self.en_qtd3.insert(END, col13)
            self.en_acond3.insert(END, col14)
            self.en_cod4.insert(END, col15)
            self.en_prod4.insert(END, col16)
            self.en_qtd4.insert(END, col17)
            self.en_acond4.insert(END, col18)
            self.en_cod5.insert(END, col19)
            self.en_prod5.insert(END, col20)
            self.en_qtd5.insert(END, col21)
            self.en_acond5.insert(END, col22)
            self.en_cod6.insert(END, col23)
            self.en_prod6.insert(END, col24)
            self.en_qtd6.insert(END, col25)
            self.en_acond6.insert(END, col26)
            self.en_cod7.insert(END, col27)
            self.en_prod7.insert(END, col28)
            self.en_qtd7.insert(END, col29)
            self.en_acond7.insert(END, col30)
            self.en_cod8.insert(END, col31)
            self.en_prod8.insert(END, col32)
            self.en_qtd8.insert(END,   col33)
            self.en_acond8.insert(END, col34)
            self.en_data.insert(END, col35)

    def Sobre(self):
        popup = Tk()
        popup.title('Sobre o criador')
        popup.geometry("+500+300")
        label1 = Label(popup, text='Criado por Wrayan Motin Bontorin\nemail: wra.motin55@gmail.com\nGITHUB: WRAYAN-MOTIN-BONTORIN ',
                       font=("Arial", 12, 'bold')).pack()
        bt1 = Button(popup, text="ok", command=lambda: popup.destroy()).pack()
        popup.mainloop()

    def datahoje(self):
        dia = datetime.today()
        self.dia_formatado = datetime.strftime(dia, '%d/%m/%Y')
        self.en_data.insert(END, self.dia_formatado)

    def atualiData(self, event):
        self.en_data.delete(0, END)
        self.en_data.insert(END, self.dia_formatado)


class aplication(Funcs, Relatorios):
    def __init__(self):
        self.root = root
        self.janela()
        self.frames_de_tela()
        self.widgets_frame_1()
        self.widgets_frame_3()
        self.Lista_frame_2()
        self.datahoje()
        self.monta_tabelas()
        self.select_lista()
        self.Menus()
        root.mainloop()

    def janela(self):
        self.root.title("GASTOS PARA CASA")
        self.root.configure(background=cor1)
        self.root.geometry("+150+5")
        self.root.resizable(0, 0)
        self.root.maxsize(width=1024, height=800)
        self.root.minsize(width=1024, height=800)

    def frames_de_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg=cor3,
                             highlightbackground=cor2, highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.85, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg=cor3,
                             highlightbackground=cor2, highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

        self.frame_3 = Frame(self.root, bd=4, bg=cor3,
                             highlightbackground=cor2, highlightthickness=3)
        self.frame_3.place(relx=0.88, rely=0.02, relwidth=0.10, relheight=0.46)

    def widgets_frame_3(self):
        # criando botao limpar
        self.btn_Limpar = Button(self.frame_3, text="Salvar", bd=2, bg=cor4, font=(
            "verdana", 8, "bold",), command=self.adicionar_ordem)
        self.btn_Limpar.place(relx=.01, rely=.01, relwidth=.98, relheight=.12)
        # criando botao buscar
        self.btn_Buscar = Button(self.frame_3, text="Alterar", bd=2, bg=cor4, font=(
            "verdana", 8, "bold"), command=self.alterar_ordem)
        self.btn_Buscar.place(relx=.01, rely=.15, relwidth=.98, relheight=.12)
        # criando botao novo
        self.btn_Novo = Button(self.frame_3, text="Buscar por\nplaca", bd=2, bg=cor4, font=(
            "verdana", 8, "bold"), command=self.buscar_placa)
        self.btn_Novo.place(relx=.01, rely=.3, relwidth=.98, relheight=.12)
        # criando botao alterar
        self.btn_Alterar = Button(self.frame_3, text="Limpar", bd=2, bg=cor4, font=(
            "verdana", 8, "bold"), command=self.Limpa_Tela)
        self.btn_Alterar.place(relx=.01, rely=.45, relwidth=.98, relheight=.12)
        # criando botao apagar
        self.btn_Apagar = Button(self.frame_3, text="Apagar", bd=2, bg=cor4, font=(
            "verdana", 8, "bold"), command=self.apaga_ordem)
        self.btn_Apagar.place(relx=.01, rely=.6, relwidth=.98, relheight=.12)
        # botao imprimir
        self.btn_Imprimir = Button(self.frame_3, text="Imprimir", bd=2, bg=cor4, font=(
            "verdana", 8, "bold"), command=self.Gerar_relatorio)
        self.btn_Imprimir.place(relx=.01, rely=.8, relwidth=.98, relheight=.12)

    def widgets_frame_1(self):
        # inserindo data
        self.data = Label(self.frame_1, text="DATA:", bg=cor3, font=(
            "Helvetica", 12, "bold")).place(relx=.62, rely=.001, relwidth=.1, relheight=.07)
        self.en_data = Entry(self.frame_1, bd=2)
        self.en_data.place(rely=.001, relx=.7, relwidth=.08, relheight=.07)
        self.en_data.bind('<Return>', self.atualiData)
        self.en_data.bind('<space>', self.atualiData)
        self.en_data.bind('<Tab>', self.atualiData)

# criacao label e entrada da ordem
        self.lb_ordem = Label(self.frame_1, text="ORDEM:", bg=cor3, font=(
            "Helvetica", 12, "bold")).place(relx=.79, rely=.001, relwidth=.1, relheight=.1)
        self.en_ordem = Entry(self.frame_1, bd=2)
        self.en_ordem.place(relx=.88, rely=.01, relwidth=.1, relheight=.08)

        # criando label e entrada da Placa
        self.lb_placa = Label(self.frame_1, text="PLACA:", bg=cor3, font=(
            "Helvetica", 18, "bold")).place(relx=.2, rely=.001, relwidth=.1, relheight=.1)
        self.en_placa = Entry(self.frame_1, bd=2,
                              font=("Helvetica", 12, "bold"))
        self.en_placa.place(relx=.31, rely=.01, relwidth=.25, relheight=.1)


#############################################################################################################################################################

        # implantacao do codigo
        self.lb_cod = Label(self.frame_1, text="CODIGO", bg=cor3, font=(
            "Helvetica", 14, "bold")).place(relx=.01, rely=.1, relwidth=.25, relheight=.12)
        self.en_cod1 = Entry(self.frame_1, bd=2)
        self.en_cod1.place(relx=.03, rely=.2, relwidth=.2, relheight=.09)

        self.en_cod2 = Entry(self.frame_1, bd=2)
        self.en_cod2.place(relx=.03, rely=.3, relwidth=.2, relheight=.09)

        self.en_cod3 = Entry(self.frame_1, bd=2)
        self.en_cod3.place(relx=.03, rely=.4, relwidth=.2, relheight=.09)

        self.en_cod4 = Entry(self.frame_1, bd=2)
        self.en_cod4.place(relx=.03, rely=.5, relwidth=.2, relheight=.09)

        self.en_cod5 = Entry(self.frame_1, bd=2)
        self.en_cod5.place(relx=.03, rely=.6, relwidth=.2, relheight=.09)

        self.en_cod6 = Entry(self.frame_1, bd=2)
        self.en_cod6.place(relx=.03, rely=.7, relwidth=.2, relheight=.09)

        self.en_cod7 = Entry(self.frame_1, bd=2)
        self.en_cod7.place(relx=.03, rely=.8, relwidth=.2, relheight=.09)

        self.en_cod8 = Entry(self.frame_1, bd=2)
        self.en_cod8.place(relx=.03, rely=.9, relwidth=.2, relheight=.09)

        # criando label e entrada da PRODUTO
        self.lb_prod1 = Label(self.frame_1, text="PRODUTO", bg=cor3, font=(
            "Helvetica", 14, "bold")).place(relx=.26, rely=.1, relwidth=.35, relheight=.12)
        self.en_prod1 = Entry(self.frame_1, bd=2)
        self.en_prod1.place(relx=.26, rely=.2, relwidth=.35, relheight=.09)

        self.en_prod2 = Entry(self.frame_1, bd=2)
        self.en_prod2.place(relx=.26, rely=.3, relwidth=.35, relheight=.09)

        self.en_prod3 = Entry(self.frame_1, bd=2)
        self.en_prod3.place(relx=.26, rely=.4, relwidth=.35, relheight=.09)

        self.en_prod4 = Entry(self.frame_1, bd=2)
        self.en_prod4.place(relx=.26, rely=.5, relwidth=.35, relheight=.09)

        self.en_prod5 = Entry(self.frame_1, bd=2)
        self.en_prod5.place(relx=.26, rely=.6, relwidth=.35, relheight=.09)

        self.en_prod6 = Entry(self.frame_1, bd=2)
        self.en_prod6.place(relx=.26, rely=.7, relwidth=.35, relheight=.09)

        self.en_prod7 = Entry(self.frame_1, bd=2)
        self.en_prod7.place(relx=.26, rely=.8, relwidth=.35, relheight=.09)

        self.en_prod8 = Entry(self.frame_1, bd=2)
        self.en_prod8.place(relx=.26, rely=.9, relwidth=.35, relheight=.09)

        # criando label e entrada da QTD
        self.lb_qtd = Label(self.frame_1, text="QTD", bg=cor3, font=(
            "Helvetica", 12, "bold")).place(relx=.65, rely=.1, relwidth=.08, relheight=.05)
        self.en_qtd1 = Entry(self.frame_1, bd=2)
        self.en_qtd1.place(relx=.65, rely=.2, relwidth=.08, relheight=.09)

        self.en_qtd2 = Entry(self.frame_1, bd=2)
        self.en_qtd2.place(relx=.65, rely=.3, relwidth=.08, relheight=.09)

        self.en_qtd3 = Entry(self.frame_1, bd=2)
        self.en_qtd3.place(relx=.65, rely=.4, relwidth=.08, relheight=.09)

        self.en_qtd4 = Entry(self.frame_1, bd=2)
        self.en_qtd4.place(relx=.65, rely=.5, relwidth=.08, relheight=.09)

        self.en_qtd5 = Entry(self.frame_1, bd=2)
        self.en_qtd5.place(relx=.65, rely=.6, relwidth=.08, relheight=.09)

        self.en_qtd6 = Entry(self.frame_1, bd=2)
        self.en_qtd6.place(relx=.65, rely=.7, relwidth=.08, relheight=.09)

        self.en_qtd7 = Entry(self.frame_1, bd=2)
        self.en_qtd7.place(relx=.65, rely=.8, relwidth=.08, relheight=.09)

        self.en_qtd8 = Entry(self.frame_1, bd=2)
        self.en_qtd8.place(relx=.65, rely=.9, relwidth=.08, relheight=.09)

        # criando label  e entrada de ACONDICIONAMENTO
        self.lb_acond = Label(self.frame_1, text="ACONDICIONAMENTO", bg=cor3, font=(
            "Helvetica", 12, "bold")).place(relx=.77, rely=.1, relwidth=.2, relheight=.09)
        self.en_acond1 = Entry(self.frame_1, bd=2)
        self.en_acond1.place(relx=.77, rely=.2, relwidth=.2, relheight=.09)

        self.en_acond2 = Entry(self.frame_1, bd=2)
        self.en_acond2.place(relx=.77, rely=.3, relwidth=.2, relheight=.09)

        self.en_acond3 = Entry(self.frame_1, bd=2)
        self.en_acond3.place(relx=.77, rely=.4, relwidth=.2, relheight=.09)

        self.en_acond4 = Entry(self.frame_1, bd=2)
        self.en_acond4.place(relx=.77, rely=.5, relwidth=.2, relheight=.09)

        self.en_acond5 = Entry(self.frame_1, bd=2)
        self.en_acond5.place(relx=.77, rely=.6, relwidth=.2, relheight=.09)

        self.en_acond6 = Entry(self.frame_1, bd=2)
        self.en_acond6.place(relx=.77, rely=.7, relwidth=.2, relheight=.09)

        self.en_acond7 = Entry(self.frame_1, bd=2)
        self.en_acond7.place(relx=.77, rely=.8, relwidth=.2, relheight=.09)

        self.en_acond8 = Entry(self.frame_1, bd=2)
        self.en_acond8.place(relx=.77, rely=.9, relwidth=.2, relheight=.09)

    def Lista_frame_2(self):
        # criando as colunas da treeview
        self.Ordem_carregamento = ttk.Treeview(self.frame_2, height=.1, column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10", "col11", "col12", "col13", "col14",
                                               "col15", "col16", "col17", "col18", "col19", "col20", "col21", "col22", "col23", "col24", "col25", "col26", "col27", "col28", "col29", "col30", "col31", "col32", "col33", "col34", "col35"))
        # criando cabeçalho das colunas
        self.Ordem_carregamento.heading("#0",  text="")
        self.Ordem_carregamento.heading("#1",  text="ordem")
        self.Ordem_carregamento.heading("#2",  text="placa")
        self.Ordem_carregamento.heading("#3",  text="cod1")
        self.Ordem_carregamento.heading("#4",  text="prod1")
        self.Ordem_carregamento.heading("#5",  text="qtd1")
        self.Ordem_carregamento.heading("#6",  text="acond1")
        self.Ordem_carregamento.heading("#7",  text="cod2")
        self.Ordem_carregamento.heading("#8",  text="prod2")
        self.Ordem_carregamento.heading("#9",  text="qtd2")
        self.Ordem_carregamento.heading("#10", text="acond2")
        self.Ordem_carregamento.heading("#11", text="cod3")
        self.Ordem_carregamento.heading("#12", text="prod3")
        self.Ordem_carregamento.heading("#13", text="qtd3")
        self.Ordem_carregamento.heading("#14", text="acond3")
        self.Ordem_carregamento.heading("#15", text="cod4")
        self.Ordem_carregamento.heading("#16", text="prod4")
        self.Ordem_carregamento.heading("#17", text="qtd4")
        self.Ordem_carregamento.heading("#18", text="acond4")
        self.Ordem_carregamento.heading("#19", text="cod5")
        self.Ordem_carregamento.heading("#20", text="prod5")
        self.Ordem_carregamento.heading("#21", text="qtd5")
        self.Ordem_carregamento.heading("#22", text="acond5")
        self.Ordem_carregamento.heading("#23", text="cod6")
        self.Ordem_carregamento.heading("#24", text="prod6")
        self.Ordem_carregamento.heading("#25", text="qtd6")
        self.Ordem_carregamento.heading("#26", text="acond6")
        self.Ordem_carregamento.heading("#27", text="cod7")
        self.Ordem_carregamento.heading("#28", text="prod7")
        self.Ordem_carregamento.heading("#29", text="qtd7")
        self.Ordem_carregamento.heading("#30", text="acond7")
        self.Ordem_carregamento.heading("#31", text="cod8")
        self.Ordem_carregamento.heading("#32", text="prod8")
        self.Ordem_carregamento.heading("#33", text="qtd8")
        self.Ordem_carregamento.heading("#34", text="acond8")
        self.Ordem_carregamento.heading("#35", text="data")

        # especificar o tamanho das colunas em relacao a lista
        self.Ordem_carregamento.column("#0",  width=1)
        self.Ordem_carregamento.column("#1",  width=70)
        self.Ordem_carregamento.column("#2",  width=70)
        self.Ordem_carregamento.column("#3",  width=70)
        self.Ordem_carregamento.column("#4",  width=70)
        self.Ordem_carregamento.column("#5",  width=70)
        self.Ordem_carregamento.column("#6",  width=70)
        self.Ordem_carregamento.column("#7",  width=70)
        self.Ordem_carregamento.column("#8",  width=70)
        self.Ordem_carregamento.column("#9",  width=70)
        self.Ordem_carregamento.column("#10", width=70)
        self.Ordem_carregamento.column("#11", width=70)
        self.Ordem_carregamento.column("#12", width=70)
        self.Ordem_carregamento.column("#13", width=70)
        self.Ordem_carregamento.column("#14", width=70)
        self.Ordem_carregamento.column("#15", width=70)
        self.Ordem_carregamento.column("#16", width=70)
        self.Ordem_carregamento.column("#17", width=70)
        self.Ordem_carregamento.column("#18", width=70)
        self.Ordem_carregamento.column("#19", width=70)
        self.Ordem_carregamento.column("#20", width=70)
        self.Ordem_carregamento.column("#21", width=70)
        self.Ordem_carregamento.column("#22", width=70)
        self.Ordem_carregamento.column("#23", width=70)
        self.Ordem_carregamento.column("#24", width=70)
        self.Ordem_carregamento.column("#25", width=70)
        self.Ordem_carregamento.column("#26", width=70)
        self.Ordem_carregamento.column("#27", width=70)
        self.Ordem_carregamento.column("#28", width=70)
        self.Ordem_carregamento.column("#29", width=70)
        self.Ordem_carregamento.column("#30", width=70)
        self.Ordem_carregamento.column("#31", width=70)
        self.Ordem_carregamento.column("#32", width=70)
        self.Ordem_carregamento.column("#33", width=70)
        self.Ordem_carregamento.column("#34", width=70)
        self.Ordem_carregamento.column("#35", width=70)
        self.Ordem_carregamento.place(
            relx=.01, rely=.01, relheight=.9, relwidth=.97,)

        # criando scrollbar

        self.scroollistay = Scrollbar(self.frame_2, orient='vertical')
        self.Ordem_carregamento.configure(yscroll=self.scroollistay.set)
        self.scroollistay.place(
            relx=.98, rely=.01, relwidth=.02, relheight=.85)

        # self.scroollistax = Scrollbar(self.frame_2, orient='horizontal')
        # self.Ordem_carregamento.configure(xscrollcommand=self.scroollistax.set)
        # self.scroollistax.place(relx=.001, rely=.95, relwidth=.99, relheight=.05)

        self.Ordem_carregamento.bind('<Double-1>', self.on_doubleclick)

    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        # criar abas de menu
        menubar.add_cascade(label="Arquivo", menu=filemenu)
        menubar.add_cascade(label="Informacao", menu=filemenu2)

        # inserir menus dentro das abas

        filemenu.add_command(label="imprimir", command=self.Gerar_relatorio)
        filemenu.add_command(label="Sair", command=Quit)

        filemenu2.add_command(label="Sobre", command=self.Sobre)


aplication()
