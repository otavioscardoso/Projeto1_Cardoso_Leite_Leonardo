import tkinter as tk

from random import randint

import winsound

import time

class Classico:
    def __init__(self):
        self.window_classico = tk.Tk()
        self.window_classico.config(background = 'black')
        self.window_classico.title("Modo clássico")
        self.window_classico.geometry("700x700")
        
        self.window_classico.rowconfigure(0, minsize=10, weight=1)
        self.window_classico.rowconfigure(1, minsize=10, weight=1)
        self.window_classico.rowconfigure(2, minsize=10, weight=1)
        self.window_classico.rowconfigure(3, minsize=10, weight=1)
        self.window_classico.rowconfigure(4, minsize=10, weight=1)
        self.window_classico.rowconfigure(5, minsize=10, weight=1)
        self.window_classico.rowconfigure(6, minsize=10, weight=1)
        
        self.window_classico.columnconfigure(0, minsize=50, weight=1)
        self.window_classico.columnconfigure(1, minsize=100, weight=1)
        self.window_classico.columnconfigure(2, minsize=100, weight=1)
        self.window_classico.columnconfigure(3, minsize=100, weight=1)
        self.window_classico.columnconfigure(4, minsize=100, weight=1)
        self.window_classico.columnconfigure(5, minsize=50, weight=1)
        
        self.iniciar = False
        self.botao_clicado = False
        self.cria_jogada=[]
        self.jogada_usuario=[]
        self.tempo = 1
        self.numero_botao = 0
        self.label_pontuacao_classico = tk.StringVar()
        self.label_pontuacao_classico.set("NÍVEL: 1")
        
        self.pontos_classico = tk.Label(self.window_classico)
        self.pontos_classico.grid(row=6, column=4, columnspan=2, sticky="nsew")
        self.pontos_classico.configure(textvariable=self.label_pontuacao_classico,font='Broadway 18', background='black', fg = 'cyan')
        
        self.titulo = tk.Label(self.window_classico)
        self.titulo.grid(row=0, column=1, columnspan=4, sticky="nsew")
        self.titulo.configure(text = 'CLÁSSICO', font='Broadway 64', fg = 'cyan', background='black')

        self.botao0 = tk.Button(self.window_classico)
        self.botao0.grid(row=1, column=1, columnspan=2, rowspan=2, sticky="nsew")
        self.botao0.configure(activebackground = 'pale goldenrod', background = 'yellow', borderwidth=12, command = self.click_botao0)
         
        self.botao1 = tk.Button(self.window_classico)
        self.botao1.grid(row=3, column=1, columnspan=2, rowspan=2, sticky="nsew")
        self.botao1.configure(activebackground = 'pale green', background = 'green2', borderwidth=12, command = self.click_botao1)
          
        self.botao2 = tk.Button(self.window_classico)
        self.botao2.grid(row=1, column=3, columnspan=2, rowspan=2, sticky="nsew")
        self.botao2.configure(activebackground = 'tomato', background = 'red', borderwidth=12, command = self.click_botao2)

        self.botao3 = tk.Button(self.window_classico)
        self.botao3.grid(row=3, column=3, columnspan=2, rowspan=2, sticky="nsew")
        self.botao3.configure(activebackground = 'sky blue', background = 'blue', borderwidth=12, command = self.click_botao3)
        
        self.botaoiniciar = tk.Button(self.window_classico)
        self.botaoiniciar.grid(row=6, column=2, columnspan = 2, sticky="nsew")
        self.botaoiniciar.configure(relief = 'ridge', text="INICIAR", borderwidth=6, activebackground = 'green2', background='black', fg = 'cyan', font='Broadway 16', command = self.botaoiniciar_teste)
          
    def botaoiniciar_teste(self):
        self.botaoiniciar.destroy()        
        self.realiza_jogadas()
    
    def click_botao0(self):
        winsound.Beep(3000,int(700*self.tempo))
        self.jogada_usuario.append(0)
        self.verifica_jogadas()
        
    def click_botao1(self):
        winsound.Beep(2500,int(700*self.tempo))       
        self.jogada_usuario.append(1)
        self.verifica_jogadas()
        
    def click_botao2(self): 
        winsound.Beep(2000,int(700*self.tempo)) 
        self.jogada_usuario.append(2)
        self.verifica_jogadas()
        
    def click_botao3(self):
        winsound.Beep(1500,int(700*self.tempo))
        self.jogada_usuario.append(3)
        self.verifica_jogadas()
    
    def piscar(self):
        for i in range (len(self.cria_jogada)):
            if self.cria_jogada[i] == 0:
                self.botao0.configure(background = 'pale goldenrod')
                self.window_classico.update()
                winsound.Beep(3000,int(700*self.tempo))
                time.sleep(self.tempo * 0.40)
                self.botao0.configure(background = 'yellow')
            elif self.cria_jogada[i] == 1:
                self.botao1.configure(background = 'pale green')
                self.window_classico.update()
                winsound.Beep(2500,int(700*self.tempo))
                time.sleep(self.tempo * 0.40)
                self.botao1.configure(background = 'green2')
            elif self.cria_jogada[i] == 2:
                self.botao2.configure(background = 'coral1')
                self.window_classico.update()
                winsound.Beep(2000,int(700*self.tempo))
                time.sleep(self.tempo * 0.40)
                self.botao2.configure(background = 'red')
            elif self.cria_jogada[i] == 3:
                self.botao3.configure(background = 'sky blue')
                self.window_classico.update()
                winsound.Beep(1500,int(700*self.tempo))
                time.sleep(self.tempo * 0.40)
                self.botao3.configure(background = 'blue')
            self.window_classico.update()
            if i != (len(self.cria_jogada) - 1):
                time.sleep(self.tempo)
        
    def realiza_jogadas(self):
        self.botao0.configure(state = 'disabled')
        self.botao1.configure(state = 'disabled')
        self.botao2.configure(state = 'disabled')
        self.botao3.configure(state = 'disabled')
        self.nivel = str(len(self.cria_jogada) + 1)
        self.label_pontuacao_classico.set("NÍVEL: {0}".format(self.nivel))
        print(self.label_pontuacao_classico.get())
        self.cria_jogada.append(randint(0,3))
        self.piscar()
        self.numero_botao = 0
        self.botao0.configure(state = 'normal')
        self.botao1.configure(state = 'normal')
        self.botao2.configure(state = 'normal')
        self.botao3.configure(state = 'normal')
            
    def verifica_jogadas(self):
        if self.jogada_usuario[self.numero_botao] != self.cria_jogada[self.numero_botao]:
            self.cria_jogada = []
            self.jogada_usuario = []
            self.erro()
        self.numero_botao += 1
        self.window_classico.update()
        if self.numero_botao == len(self.cria_jogada):  
            time.sleep(1)
            self.tempo = self.tempo * 0.90
            self.jogada_usuario = []
            self.realiza_jogadas()
    
    def erro(self):
        winsound.PlaySound('Fail',winsound.SND_FILENAME)
        self.tempo = 1
        self.botao0.destroy()
        self.botao1.destroy()
        self.botao2.destroy()
        self.botao3.destroy()
        self.perdeu = tk.Label(self.window_classico)
        self.perdeu.grid(row=1, column=1, columnspan=4, rowspan=4, sticky="nsew")
        self.perdeu.configure(text="VOCÊ PERDEU...", font='Broadway 42', background='black', fg = 'cyan')
        self.botaoreiniciar = tk.Button(self.window_classico)
        self.botaoreiniciar.grid(row=6, column=2, columnspan = 2, sticky="nsew")
        self.botaoreiniciar.configure(relief = 'ridge', text="REINICIAR", borderwidth=6, activebackground = 'green2', background='black', fg = 'cyan', font='Broadway 16')
        self.botaoreiniciar.configure(command =lambda: self.botaoreiniciar_teste())
        
    def botaoreiniciar_teste(self):
        self.botaoreiniciar.destroy()
        
        self.botao0 = tk.Button(self.window_classico)
        self.botao0.grid(row=1, column=1, columnspan=2, rowspan=2, sticky="nsew")
        self.botao0.configure(activebackground = 'pale goldenrod', background = 'yellow', borderwidth=12, command = self.click_botao0)
         
        self.botao1 = tk.Button(self.window_classico)
        self.botao1.grid(row=3, column=1, columnspan=2, rowspan=2, sticky="nsew")
        self.botao1.configure(activebackground = 'pale green', background = 'green2', borderwidth=12, command = self.click_botao1)
          
        self.botao2 = tk.Button(self.window_classico)
        self.botao2.grid(row=1, column=3, columnspan=2, rowspan=2, sticky="nsew")
        self.botao2.configure(activebackground = 'coral1', background = 'red', borderwidth=12, command = self.click_botao2)

        self.botao3 = tk.Button(self.window_classico)
        self.botao3.grid(row=3, column=3, columnspan=2, rowspan=2, sticky="nsew")
        self.botao3.configure(activebackground = 'sky blue', background = 'blue', borderwidth=12, command = self.click_botao3)
        
        self.window_classico.update()
        time.sleep(0.5)
        self.realiza_jogadas()
    
  
    def iniciar_classico(self):
        self.window_classico.mainloop()