import tkinter as tk
import random
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
        self.label_pontuacao.set("NÍVEL: 0")
        self.lista_musicas = [ self.winsound.PlaySound('Love',winsound.SND_FILENAME), self.winsound.PlaySound('Birds',winsound.SND_FILENAME), self.winsound.PlaySound('Sherif',winsound.SND_FILENAME), self.winsound.PlaySound('Woman',winsound.SND_FILENAME)]
        
        
        
        self.pontos = tk.Label(self.window_musica)
        self.pontos.grid(row=6, column=4, columnspan=2, sticky="nsew")
        self.pontos.configure(text="NÍVEL: {0}".format(self.label_pontuacao),textvariable=self.label_pontuacao, font='Broadway 18', background='black', fg = 'cyan')
        
        self.titulo = tk.Label(self.window_musica)
        self.titulo.grid(row=0, column=1, columnspan=4, sticky="nsew")
        self.titulo.configure(text = 'MÚSICA', font='Broadway 64', fg = 'cyan', background='black')
        
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
        self.botaoiniciar.configure(relief = 'ridge', text="INICIAR", borderwidth=6, activebackground = 'green2', background='black', fg = 'cyan', font='Broadway 16', command = self.botaoiniciar_teste)
          
        self.botaomenu = tk.Button(self.window_musica)
        self.botaomenu.grid(row=6, column=0, columnspan = 2, sticky="nsew")
        self.botaomenu.configure(relief = 'ridge', text="MENU", borderwidth=6, activebackground = 'green2', background='black', fg = 'cyan', font='Broadway 16')   
   
    def toca_musicas(self):
        a = random(self.lista_musicas)
        a
        
        
    def frame_musica(self):
        self.botao0.destroy()
        self.botao1.destroy()
        self.botao2.destroy()
        self.botao3.destroy()        
        
        self.pergunta = tk.Label(self.window_musica)
        self.pergunta.grid(row=1, column=1, columnspan=4, sticky="nsew")
        self.pergunta.configure(text="Que música estava tocando?", font='Broadway 18', background='black', fg = 'cyan')        
        
        self.botao_musica1 = tk.Button(self.window_musica)
        self.botao_musica1.grid(row=2, column=1, columnspan=4, sticky="nsew")
        self.botao_musica1.configure(activebackground = 'pale green', background = 'green2', borderwidth=12, text="musica 1")
        
        self.botao_musica2 = tk.Button(self.window_musica)
        self.botao_musica2.grid(row=3, column=1, columnspan=4, sticky="nsew")
        self.botao_musica2.configure(activebackground = 'pale green', background = 'green2', borderwidth=12, text="musica 2")
        
        self.botao_musica3 = tk.Button(self.window_musica)
        self.botao_musica3.grid(row=4, column=1, columnspan=4, sticky="nsew")
        self.botao_musica3.configure(activebackground = 'pale green', background = 'green2', borderwidth=12, text="musica 3")
        
        self.botao_musica4 = tk.Button(self.window_musica)
        self.botao_musica4.grid(row=5, column=1, columnspan=4, sticky="nsew")
        self.botao_musica4.configure(activebackground = 'pale green', background = 'green2', borderwidth=12, text="musica 4")
        
        self.botao_musica5 = tk.Button(self.window_musica)
        self.botao_musica5.grid(row=5, column=1, columnspan=4, sticky="nsew")
        self.botao_musica5.configure(activebackground = 'pale green', background = 'green2', borderwidth=12, text="Continuar jogo")
  
    #def verifica_musica(self):
     #   if musica escolhida = self.a:
      #      acerto()
       # elif musica escolhida = continuar jogando:
        #    voltar ao frame antigo
        #elif musica escolhida != self.a:
         #   erro()
  
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
                self.window_musica.update()
                winsound.Beep(3000,int(700*self.tempo))
                time.sleep(self.tempo * 0.40)
                self.botao0.configure(background = 'yellow')
            elif self.cria_jogada[i] == 1:
                self.botao1.configure(background = 'pale green')
                self.window_musica.update()
                winsound.Beep(2500,int(700*self.tempo))
                time.sleep(self.tempo * 0.40)
                self.botao1.configure(background = 'green2')
            elif self.cria_jogada[i] == 2:
                self.botao2.configure(background = 'coral1')
                self.window_musica.update()
                winsound.Beep(2000,int(700*self.tempo))
                time.sleep(self.tempo * 0.40)
                self.botao2.configure(background = 'red')
            elif self.cria_jogada[i] == 3:
                self.botao3.configure(background = 'sky blue')
                self.window_musica.update()
                winsound.Beep(1500,int(700*self.tempo))
                time.sleep(self.tempo * 0.40)
                self.botao3.configure(background = 'blue')
            self.window_musica.update()
            if i != (len(self.cria_jogada) - 1):
                time.sleep(self.tempo)
        
    def realiza_jogadas(self):
        self.botao0.configure(state = 'disabled')
        self.botao1.configure(state = 'disabled')
        self.botao2.configure(state = 'disabled')
        self.botao3.configure(state = 'disabled')
        self.nivel = str(len(self.cria_jogada))
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
        winsound.PlaySound('Fail',winsound.SND_FILENAME)
        self.tempo = 1
        self.botao0.destroy()
        self.botao1.destroy()
        self.botao2.destroy()
        self.botao3.destroy()
        self.perdeu = tk.Label(self.window_musica)
        self.perdeu.grid(row=1, column=1, columnspan=4, rowspan=4, sticky="nsew")
        self.perdeu.configure(text="VOCÊ PERDEU...", font='Broadway 42', background='black', fg = 'cyan')
        self.botaoreiniciar = tk.Button(self.window_musica)
        self.botaoreiniciar.grid(row=6, column=2, columnspan = 2, sticky="nsew")
        self.botaoreiniciar.configure(relief = 'ridge', text="REINICIAR", borderwidth=6, activebackground = 'green2', background='black', fg = 'cyan', font='Broadway 16')
        self.botaoreiniciar.configure(command =lambda: self.botaoreiniciar_teste())
        
    def acerto(self):
        self.tempo = 1
        self.botao0.destroy()
        self.botao1.destroy()
        self.botao2.destroy()
        self.botao3.destroy()
        self.venceu = tk.Label(self.window_musica)
        self.venceu.grid(row=1, column=1, columnspan=4, rowspan=4, sticky="nsew")
        self.venceu.configure(text="Parabéns, você venceu em x niveis", font='Broadway 42', background='black', fg = 'cyan')
        self.botaoreiniciar = tk.Button(self.window_musica)
        self.botaoreiniciar.grid(row=6, column=2, columnspan = 2, sticky="nsew")
        self.botaoreiniciar.configure(relief = 'ridge', text="REINICIAR", borderwidth=6, activebackground = 'green2', background='black', fg = 'cyan', font='Broadway 16')
        self.botaoreiniciar.configure(command =lambda: self.botaoreiniciar_teste())
        
    def botaoreiniciar_teste(self):
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
        self.realiza_jogadas()
        
    def adivinhar_musica(self):
        print("oi")
        
         
    def quit(self):
        self.window.destroy()
  
    def iniciar_musica(self):
        self.window_musica.mainloop()
