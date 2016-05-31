import tkinter as tk

from random import *

import winsound

import time

class Musica:
    def __init__(self):
        self.window_musica = tk.Tk()
        self.window_musica.config(background = 'black')
        self.window_musica.title("Modo clássico")
        self.window_musica.geometry("700x700")
        
        self.window_musica.rowconfigure(0, minsize=10, weight=1)
        self.window_musica.rowconfigure(1, minsize=10, weight=1)
        self.window_musica.rowconfigure(2, minsize=10, weight=1)
        self.window_musica.rowconfigure(3, minsize=10, weight=1)
        self.window_musica.rowconfigure(4, minsize=10, weight=1)
        self.window_musica.rowconfigure(5, minsize=10, weight=1)
        self.window_musica.rowconfigure(6, minsize=10, weight=1)
        
        self.window_musica.columnconfigure(0, minsize=50, weight=1)
        self.window_musica.columnconfigure(1, minsize=100, weight=1)
        self.window_musica.columnconfigure(2, minsize=100, weight=1)
        self.window_musica.columnconfigure(3, minsize=100, weight=1)
        self.window_musica.columnconfigure(4, minsize=100, weight=1)
        self.window_musica.columnconfigure(5, minsize=50, weight=1)
        
        self.iniciar = False
        self.botao_clicado = False
        self.cria_jogada=[]
        self.jogada_usuario=[]
        self.tempo = 1
        self.numero_botao = 0
        self.label_pontuacao = tk.StringVar()
        self.label_pontuacao.set("NÍVEL: 1")
        self.lista_musicas = ["One Love", "No Woman No Cry", "Three Little Birds", "I Shot The Sheriff"]
        self.musica_tocando = None
        self.musica_escolhida =None
        
        
        self.pontos = tk.Label(self.window_musica)
        self.pontos.grid(row=6, column=4, columnspan=2, sticky="nsew")
        self.pontos.configure(textvariable=self.label_pontuacao, font='Broadway 18', background='black', fg = 'purple1')
        
        self.titulo = tk.Label(self.window_musica)
        self.titulo.grid(row=0, column=1, columnspan=4, sticky="nsew")
        self.titulo.configure(text = 'MÚSICA', font='Broadway 64', fg = 'purple1', background='black')
        
        self.botao0 = tk.Button(self.window_musica)
        self.botao0.grid(row=1, column=1, columnspan=2, rowspan=2, sticky="nsew")
        self.botao0.configure(activebackground = 'pale goldenrod', background = 'yellow', borderwidth=12, command = self.click_botao0)
         
        self.botao1 = tk.Button(self.window_musica)
        self.botao1.grid(row=3, column=1, columnspan=2, rowspan=2, sticky="nsew")
        self.botao1.configure(activebackground = 'pale green', background = 'green2', borderwidth=12, command = self.click_botao1)
          
        self.botao2 = tk.Button(self.window_musica)
        self.botao2.grid(row=1, column=3, columnspan=2, rowspan=2, sticky="nsew")
        self.botao2.configure(activebackground = 'tomato', background = 'red', borderwidth=12, command = self.click_botao2)
        
        self.botao3 = tk.Button(self.window_musica)
        self.botao3.grid(row=3, column=3, columnspan=2, rowspan=2, sticky="nsew")
        self.botao3.configure(activebackground = 'sky blue', background = 'blue', borderwidth=12, command = self.click_botao3)
        
        self.botaoiniciar = tk.Button(self.window_musica)
        self.botaoiniciar.grid(row=6, column=2, columnspan = 2, sticky="nsew")
        self.botaoiniciar.configure(command =lambda: self.iniciar_jogo(), relief = 'ridge', text="INICIAR", borderwidth=6, activebackground = 'green2', background='black', fg = 'purple1', font='Broadway 16')
          
    def toca_musicas(self):     
        self.musica_tocando = randint(0,3)
        if self.musica_tocando == 0:
            winsound.PlaySound('One Love',winsound.SND_ASYNC)
        elif self.musica_tocando == 1:
            winsound.PlaySound('No Woman No Cry',winsound.SND_ASYNC)
        elif self.musica_tocando == 2:
            winsound.PlaySound('Three Little Birds',winsound.SND_ASYNC)
        elif self.musica_tocando == 3:
            winsound.PlaySound('I Shot The Sheriff',winsound.SND_ASYNC)
            
    def iniciar_jogo(self):
        self.botaoiniciar.destroy()        
        self.realiza_jogadas()
        self.toca_musicas()
    
    def frame_musica(self):
        winsound.PlaySound(None,winsound.SND_ASYNC)
        self.botao0.destroy()
        self.botao1.destroy()
        self.botao2.destroy()
        self.botao3.destroy()        
        
        self.pergunta = tk.Label(self.window_musica)
        self.pergunta.grid(row=1, column=1, columnspan=4, sticky="nsew")
        self.pergunta.configure(text="Que música estava tocando?", font='Broadway 18', background='black', fg = 'purple1')        
        
        self.botao_musica0 = tk.Button(self.window_musica)
        self.botao_musica0.grid(row=2, column=1, columnspan=4, sticky="nsew")
        self.botao_musica0.configure(command =lambda: self.escolher_musica0(),font='Broadway 15', activebackground = 'pale green', background = 'green2', borderwidth=12, text=self.lista_musicas[0])
        
        self.botao_musica1 = tk.Button(self.window_musica)
        self.botao_musica1.grid(row=3, column=1, columnspan=4, sticky="nsew")
        self.botao_musica1.configure(command =lambda: self.escolher_musica1(),font='Broadway 15', activebackground = 'pale green', background = 'green2', borderwidth=12, text=self.lista_musicas[1])
        
        self.botao_musica2 = tk.Button(self.window_musica)
        self.botao_musica2.grid(row=4, column=1, columnspan=4, sticky="nsew")
        self.botao_musica2.configure(command =lambda: self.escolher_musica2(),font='Broadway 15', activebackground = 'pale green', background = 'green2', borderwidth=12, text=self.lista_musicas[2])
        
        self.botao_musica3 = tk.Button(self.window_musica)
        self.botao_musica3.grid(row=5, column=1, columnspan=4, sticky="nsew")
        self.botao_musica3.configure(command =lambda: self.escolher_musica3(),font='Broadway 15', activebackground = 'pale green', background = 'green2', borderwidth=12, text=self.lista_musicas[3])

    def escolher_musica0(self):
        self.musica_escolhida = 0
        self.verificar_musica_escolhida()
        
    def escolher_musica1(self):
        self.musica_escolhida = 1
        self.verificar_musica_escolhida()
        
    def escolher_musica2(self):
        self.musica_escolhida = 2
        self.verificar_musica_escolhida()
  
    def escolher_musica3(self):
        self.musica_escolhida = 3
        self.verificar_musica_escolhida()
        
    def verificar_musica_escolhida(self):
        if self.musica_escolhida == self.musica_tocando:
            self.pergunta.destroy()
            self.botao_musica0.destroy()
            self.botao_musica1.destroy()
            self.botao_musica2.destroy()
            self.botao_musica3.destroy()
        
            self.botao0 = tk.Button(self.window_musica)
            self.botao0.grid(row=1, column=1, columnspan=2, rowspan=2, sticky="nsew")
            self.botao0.configure(activebackground = 'pale goldenrod', background = 'yellow', borderwidth=12, command = self.click_botao0)
         
            self.botao1 = tk.Button(self.window_musica)
            self.botao1.grid(row=3, column=1, columnspan=2, rowspan=2, sticky="nsew")
            self.botao1.configure(activebackground = 'pale green', background = 'green2', borderwidth=12, command = self.click_botao1)
            
            self.botao2 = tk.Button(self.window_musica)
            self.botao2.grid(row=1, column=3, columnspan=2, rowspan=2, sticky="nsew")
            self.botao2.configure(activebackground = 'coral1', background = 'red', borderwidth=12, command = self.click_botao2)
            
            self.botao3 = tk.Button(self.window_musica)
            self.botao3.grid(row=3, column=3, columnspan=2, rowspan=2, sticky="nsew")
            self.botao3.configure(activebackground = 'sky blue', background = 'blue', borderwidth=12, command = self.click_botao3)
            
            self.toca_musicas()
            self.botao0.configure(state = 'disabled')
            self.botao1.configure(state = 'disabled')
            self.botao2.configure(state = 'disabled')
            self.botao3.configure(state = 'disabled')
            self.nivel = str(len(self.cria_jogada) + 1)
            self.label_pontuacao.set("NÍVEL: {0}".format(self.nivel))
            self.cria_jogada.append(randint(0,3))
            self.piscar()
            self.numero_botao = 0
            self.botao0.configure(state = 'normal')
            self.botao1.configure(state = 'normal')
            self.botao2.configure(state = 'normal')
            self.botao3.configure(state = 'normal')
            
        else:
            self.erro()
            self.cria_jogada=[]
            self.jogada_usuario=[]
        self.window_musica.update()    
  
    def click_botao0(self):
        self.jogada_usuario.append(0)
        self.verifica_jogadas()
        
    def click_botao1(self):     
        self.jogada_usuario.append(1)
        self.verifica_jogadas()
        
    def click_botao2(self):
        self.jogada_usuario.append(2)
        self.verifica_jogadas()
        
    def click_botao3(self):
        self.jogada_usuario.append(3)
        self.verifica_jogadas()
    
    def piscar(self):
        for i in range (len(self.cria_jogada)):
            if self.cria_jogada[i] == 0:
                self.botao0.configure(background = 'pale goldenrod')
                self.window_musica.update()
                time.sleep(self.tempo * 0.40)
                self.botao0.configure(background = 'yellow')
            elif self.cria_jogada[i] == 1:
                self.botao1.configure(background = 'pale green')
                self.window_musica.update()
                time.sleep(self.tempo * 0.40)
                self.botao1.configure(background = 'green2')
            elif self.cria_jogada[i] == 2:
                self.botao2.configure(background = 'coral1')
                self.window_musica.update()
                time.sleep(self.tempo * 0.40)
                self.botao2.configure(background = 'red')
            elif self.cria_jogada[i] == 3:
                self.botao3.configure(background = 'sky blue')
                self.window_musica.update()
                time.sleep(self.tempo * 0.40)
                self.botao3.configure(background = 'blue')
            self.window_musica.update()
            if i != (len(self.cria_jogada) - 1):
                time.sleep(self.tempo)
        
    def realiza_jogadas(self):
        if len(self.cria_jogada)%3 == 0 and len(self.cria_jogada) > 0:
            self.frame_musica()
        else:
            self.botao0.configure(state = 'disabled')
            self.botao1.configure(state = 'disabled')
            self.botao2.configure(state = 'disabled')
            self.botao3.configure(state = 'disabled')
            self.nivel = str(len(self.cria_jogada) + 1)
            self.label_pontuacao.set("NÍVEL: {0}".format(self.nivel))
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
        self.window_musica.update()
        if self.numero_botao == len(self.cria_jogada):  
            time.sleep(1)
            self.tempo = self.tempo * 0.90
            self.jogada_usuario = []
            self.realiza_jogadas()
    
    def erro(self):
        winsound.PlaySound(None,winsound.SND_ASYNC)
        winsound.PlaySound('Fail',winsound.SND_ASYNC)
        self.tempo = 1
        if len(self.cria_jogada)%3 == 0 and len(self.cria_jogada) > 0:
            self.pergunta.destroy()
            self.botao_musica0.destroy()
            self.botao_musica1.destroy()
            self.botao_musica2.destroy()
            self.botao_musica3.destroy()
        else:
            self.botao0.destroy()
            self.botao1.destroy()
            self.botao2.destroy()
            self.botao3.destroy()
        self.perdeu = tk.Label(self.window_musica)
        self.perdeu.grid(row=1, column=1, columnspan=4, rowspan=4, sticky="nsew")
        self.perdeu.configure(text="VOCÊ PERDEU...", font='Broadway 42', background='black', fg = 'purple1')
        self.botaoreiniciar = tk.Button(self.window_musica)
        self.botaoreiniciar.grid(row=6, column=2, columnspan = 2, sticky="nsew")
        self.botaoreiniciar.configure(relief = 'ridge', text="REINICIAR", borderwidth=6, activebackground = 'green2', background='black', fg = 'purple1', font='Broadway 16')
        self.botaoreiniciar.configure(command =lambda: self.botaoreiniciar_teste())
                
    def botaoreiniciar_teste(self):
        winsound.PlaySound(None,winsound.SND_ASYNC)
        self.botaoreiniciar.destroy()
        
        self.botao0 = tk.Button(self.window_musica)
        self.botao0.grid(row=1, column=1, columnspan=2, rowspan=2, sticky="nsew")
        self.botao0.configure(activebackground = 'pale goldenrod', background = 'yellow', borderwidth=12, command = self.click_botao0)
         
        self.botao1 = tk.Button(self.window_musica)
        self.botao1.grid(row=3, column=1, columnspan=2, rowspan=2, sticky="nsew")
        self.botao1.configure(activebackground = 'pale green', background = 'green2', borderwidth=12, command = self.click_botao1)
          
        self.botao2 = tk.Button(self.window_musica)
        self.botao2.grid(row=1, column=3, columnspan=2, rowspan=2, sticky="nsew")
        self.botao2.configure(activebackground = 'coral1', background = 'red', borderwidth=12, command = self.click_botao2)
        
        self.botao3 = tk.Button(self.window_musica)
        self.botao3.grid(row=3, column=3, columnspan=2, rowspan=2, sticky="nsew")
        self.botao3.configure(activebackground = 'sky blue', background = 'blue', borderwidth=12, command = self.click_botao3)
        
        self.window_musica.update()
        time.sleep(0.5)
        self.iniciar_jogo()
  
    def iniciar_musica(self):
        self.window_musica.mainloop()