import tkinter as tk

import time

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
        
        self.nivel = 0
        self.iniciar = False
        self.cria_jogada=[]
        self.jogada_usuario=[]
        self.botao_clicado = False
        self.tempo = 1
        self.numero_botao = 0
        self.lista_real=[]
        self.lista_jogador=[]

        self.pontos = tk.Label(self.window_multijogador)
        self.pontos.grid(row=6, column=4, columnspan=2, sticky="nsew")
        self.pontos.configure(text="NÍVEL: {0}".format(self.nivel), font='Broadway 18', background='black', fg = 'cyan')
        
        self.titulo = tk.Label(self.window_multijogador)
        self.titulo.grid(row=0, column=1, columnspan=4, sticky="nsew")
        self.titulo.configure(text = 'MULTIJOGADOR', font='Broadway 43', fg = 'cyan', background='black')

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
        
        self.botaoiniciar = tk.Button(self.window_multijogador)
        self.botaoiniciar.grid(row=6, column=2, columnspan = 2, sticky="nsew")
        self.botaoiniciar.configure(relief = 'ridge', text="INICIAR", borderwidth=6, activebackground = 'green2', background='black', fg = 'cyan', font='Broadway 16', command = self.botaoiniciar_teste)
          
        self.botaomenu = tk.Button(self.window_multijogador)
        self.botaomenu.grid(row=6, column=0, columnspan = 2, sticky="nsew")
        self.botaomenu.configure(relief = 'ridge', text="MENU", borderwidth=6, activebackground = 'green2', background='black', fg = 'cyan', font='Broadway 16')   
        
    def botaoiniciar_teste(self):
        self.botaoiniciar.destroy()        
    
    def click_botao0(self):
        while len(self.lista_real)>len(self.lista_jogador):
            self.lista_jogador.append(0)
            self.verifica_jogadas()
        self.lista_real.append(0)
        
    def click_botao1(self):
        while len(self.lista_real)>len(self.lista_jogador):
            self.lista_jogador.append(1)
            self.verifica_jogadas()
        self.lista_real.append(1)
        
    def click_botao2(self):
        while len(self.lista_real)>len(self.lista_jogador):
            self.lista_jogador.append(2)
            self.verifica_jogadas()
        self.lista_real.append(2)
        
    def click_botao3(self):
        while len(self.lista_real)>len(self.lista_jogador):
             self.lista_jogador.append(3)
             self.verifica_jogadas()
        self.lista_real.append(3)
    
    def piscar(self):
        for i in self.lista_real:
            if i == 0:
                self.botao0.configure(background = 'pale goldenrod')
                self.window_multijogador.update()
                time.sleep(self.tempo * 0.70)
                self.botao0.configure(background = 'yellow')
            elif i == 1:
                self.botao1.configure(background = 'pale green')
                self.window_multijogador.update()
                time.sleep(self.tempo * 0.70)
                self.botao1.configure(background = 'green2')
            elif i == 2:
                self.botao2.configure(background = 'tomato')
                self.window_multijogador.update()
                time.sleep(self.tempo * 0.70)
                self.botao2.configure(background = 'red')
            elif i == 3:
                self.botao3.configure(background = 'sky blue')
                self.window_multijogador.update()
                time.sleep(self.tempo * 0.70)
                self.botao3.configure(background = 'blue')
            self.window_multijogador.update()
            time.sleep(self.tempo)
            
    def verifica_jogadas(self):
        if self.lista_jogador[self.numero_botao] != self.lista_real[self.numero_botao]:
            self.lista_real = []
            self.lista_jogador = []
            self.erro()
            print("Errou")
        self.numero_botao += 1
        self.window_multijogador.update()
        if self.numero_botao == len(self.lista_real):  
            time.sleep(1)
            self.tempo = self.tempo * 0.90
            print(self.tempo)
            self.nivel += 1
            self.jogada_usuario = []
    
    def erro(self):
        self.tempo = 1
        self.botao0.destroy()
        self.botao1.destroy()
        self.botao2.destroy()
        self.botao3.destroy()
        self.perdeu = tk.Label(self.window_multijogador)
        self.perdeu.grid(row=1, column=1, columnspan=4, rowspan=4, sticky="nsew")
        self.perdeu.configure(text="VOCÊ PERDEU...", font='Broadway 42', background='black', fg = 'cyan')
        self.botaoreiniciar = tk.Button(self.window_multijogador)
        self.botaoreiniciar.grid(row=6, column=2, columnspan = 2, sticky="nsew")
        self.botaoreiniciar.configure(relief = 'ridge', text="REINICIAR", borderwidth=6, activebackground = 'green2', background='black', fg = 'cyan', font='Broadway 16')
        self.botaoreiniciar.configure(command =lambda: self.botaoreiniciar_teste())

    def botaoreiniciar_teste(self):
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
        
        self.window_multijogador.update()
        time.sleep(0.5)
         
    def quit(self):
        self.window.destroy()
  
    def iniciar_multijogador(self):
        self.window_multijogador.mainloop() 
