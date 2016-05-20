import tkinter as tk

import winsound

class Multijogador:
    def __init__(self):
        self.window_multijogador = tk.Tk()
        self.window_multijogador.config(background = 'black')
        self.window_multijogador.title("Modo multijogador")
        self.window_multijogador.geometry("700x700")
        
        self.window_multijogador.rowconfigure(0, minsize=10, weight=1)
        self.window_multijogador.rowconfigure(1, minsize=10, weight=1)
        self.window_multijogador.rowconfigure(2, minsize=10, weight=1)
        self.window_multijogador.rowconfigure(3, minsize=10, weight=1)
        self.window_multijogador.rowconfigure(4, minsize=10, weight=1)
        self.window_multijogador.rowconfigure(5, minsize=10, weight=1)
        self.window_multijogador.rowconfigure(6, minsize=10, weight=1)
        
        self.window_multijogador.columnconfigure(0, minsize=100, weight=1)
        self.window_multijogador.columnconfigure(1, minsize=100, weight=1)
        self.window_multijogador.columnconfigure(2, minsize=100, weight=1)
        self.window_multijogador.columnconfigure(3, minsize=100, weight=1)
        self.window_multijogador.columnconfigure(4, minsize=100, weight=1)
        self.window_multijogador.columnconfigure(5, minsize=100, weight=1)
        
        self.rodada = 0
        self.muda_jogador = 0
        self.iniciar = False
        self.botao_clicado = False
        self.numero_botao = 0
        self.lista_real=[]
        self.lista_jogador=[]
        self.label_jogador = tk.StringVar()
        self.label_jogador.set("VEZ DE : JOGADOR 1")

        self.label_vez_jogador = tk.Label(self.window_multijogador)
        self.label_vez_jogador.grid(row=6, column=2, columnspan=4, sticky="nsew")
        self.label_vez_jogador.configure(text="VEZ DE : JOGADOR {0}".format(self.label_jogador),textvariable=self.label_jogador, font='Broadway 18', background='black', fg = 'deep pink')
        
        self.titulo = tk.Label(self.window_multijogador)
        self.titulo.grid(row=0, column=1, columnspan=4, sticky="nsew")
        self.titulo.configure(text = 'MULTIJOGADOR', font='Broadway 43', fg = 'deep pink', background='black')

        self.botao0 = tk.Button(self.window_multijogador)
        self.botao0.grid(row=1, column=1, columnspan=2, rowspan=2, sticky="nsew")
        self.botao0.configure(activebackground = 'pale goldenrod', background = 'yellow', borderwidth=12, command = self.click_botao0)
         
        self.botao1 = tk.Button(self.window_multijogador)
        self.botao1.grid(row=3, column=1, columnspan=2, rowspan=2, sticky="nsew")
        self.botao1.configure(activebackground = 'pale green', background = 'green2', borderwidth=12, command = self.click_botao1)
          
        self.botao2 = tk.Button(self.window_multijogador)
        self.botao2.grid(row=1, column=3, columnspan=2, rowspan=2, sticky="nsew")
        self.botao2.configure(activebackground = 'coral1', background = 'red', borderwidth=12, command = self.click_botao2)

        self.botao3 = tk.Button(self.window_multijogador)
        self.botao3.grid(row=3, column=3, columnspan=2, rowspan=2, sticky="nsew")
        self.botao3.configure(activebackground = 'sky blue', background = 'blue', borderwidth=12, command = self.click_botao3)
          
        self.botaomenu = tk.Button(self.window_multijogador)
        self.botaomenu.grid(row=6, column=0, columnspan = 2, sticky="nsew")
        self.botaomenu.configure(relief = 'ridge', text="MENU", borderwidth=6, activebackground = 'green2', background='black', fg = 'deep pink', font='Broadway 16')   
          
    def vez_jogador(self):
        if self.muda_jogador % 2 == 0:
            self.label_jogador.set("VEZ DE : JOGADOR {0}".format(2))
        else:
            self.label_jogador.set("VEZ DE : JOGADOR {0}".format(1))

    def click_botao0(self):
        winsound.Beep(3000, 500)
        if len(self.lista_real)==len(self.lista_jogador):
            self.lista_real.append(0)
            self.lista_jogador = []
            self.rodada = 0
            self.vez_jogador()
            self.muda_jogador += 1
        elif len(self.lista_real)>len(self.lista_jogador):
            self.lista_jogador.append(0)
            self.verifica_jogadas()
        
    def click_botao1(self):
        winsound.Beep(2500,500) 
        if len(self.lista_real)==len(self.lista_jogador):
            self.lista_real.append(1)
            self.lista_jogador = []
            self.rodada = 0
            self.vez_jogador()
            self.muda_jogador += 1
        elif len(self.lista_real)>len(self.lista_jogador):
            self.lista_jogador.append(1)
            self.verifica_jogadas()  
        
    def click_botao2(self):
        winsound.Beep(2000,500) 
        if len(self.lista_real)==len(self.lista_jogador):
            self.lista_real.append(2)
            self.lista_jogador = []
            self.rodada = 0
            self.vez_jogador()
            self.muda_jogador += 1
        elif len(self.lista_real)>len(self.lista_jogador):
            self.lista_jogador.append(2)
            self.verifica_jogadas()

    def click_botao3(self):
        winsound.Beep(1500,500)
        if len(self.lista_real)==len(self.lista_jogador):
            self.lista_real.append(3)
            self.lista_jogador = []
            self.rodada = 0
            self.vez_jogador()
            self.muda_jogador += 1
        elif len(self.lista_real)>len(self.lista_jogador):
            self.lista_jogador.append(3)
            self.verifica_jogadas()
            
    def verifica_jogadas(self):
        if self.lista_jogador[self.rodada] != self.lista_real[self.rodada]:     
            self.lista_real = []
            self.lista_jogador = []
            self.erro()
        self.rodada += 1
    
    def erro(self):
        self.botao0.destroy()
        self.botao1.destroy()
        self.botao2.destroy()
        self.botao3.destroy()
        self.botaoreiniciar = tk.Button(self.window_multijogador)
        self.botaoreiniciar.grid(row=6, column=2, columnspan = 2, sticky="nsew")
        self.botaoreiniciar.configure(relief = 'ridge', text="REINICIAR", borderwidth=6, activebackground = 'green2', background='black', fg = 'deep pink', font='Broadway 16')
        self.botaoreiniciar.configure(command =lambda: self.botaoreiniciar_teste())
        self.perdeu = tk.Label(self.window_multijogador)
        self.perdeu.grid(row=1, column=1, columnspan=4, rowspan=4, sticky="nsew")
        self.label_vez_jogador.destroy()
        if self.muda_jogador % 2 == 0:
            self.perdeu.configure(text="JOGADOR 1\n PERDEU...", font='Broadway 42', background='black', fg = 'deep pink')
        else:
            self.perdeu.configure(text="JOGADOR 2\n PERDEU...", font='Broadway 42', background='black', fg = 'deep pink')
        self.muda_jogador = 0
        winsound.PlaySound('Fail',winsound.SND_FILENAME)
        
    def botaoreiniciar_teste(self):
        self.botaoreiniciar.destroy()
        self.botao0 = tk.Button(self.window_multijogador)
        self.botao0.grid(row=1, column=1, columnspan=2, rowspan=2, sticky="nsew")
        self.botao0.configure(activebackground = 'pale goldenrod', background = 'yellow', borderwidth=12, command = self.click_botao0)
         
        self.botao1 = tk.Button(self.window_multijogador)
        self.botao1.grid(row=3, column=1, columnspan=2, rowspan=2, sticky="nsew")
        self.botao1.configure(activebackground = 'pale green', background = 'green2', borderwidth=12, command = self.click_botao1)
          
        self.botao2 = tk.Button(self.window_multijogador)
        self.botao2.grid(row=1, column=3, columnspan=2, rowspan=2, sticky="nsew")
        self.botao2.configure(activebackground = 'tomato', background = 'red', borderwidth=12, command = self.click_botao2)

        self.botao3 = tk.Button(self.window_multijogador)
        self.botao3.grid(row=3, column=3, columnspan=2, rowspan=2, sticky="nsew")
        self.botao3.configure(activebackground = 'sky blue', background = 'blue', borderwidth=12, command = self.click_botao3)
        
        self.label_jogador = tk.StringVar()
        self.label_jogador.set("VEZ DE : JOGADOR 1")
        self.muda_jogador = 0
        
        self.label_vez_jogador = tk.Label(self.window_multijogador)
        self.label_vez_jogador.grid(row=6, column=2, columnspan=4, sticky="nsew")
        self.label_vez_jogador.configure(text="VEZ DE : JOGADOR {0}".format(self.label_jogador),textvariable=self.label_jogador, font='Broadway 18', background='black', fg = 'deep pink')
                 
    def quit(self):
        self.window.destroy()
  
    def iniciar_multijogador(self):
        self.window_multijogador.mainloop() 
