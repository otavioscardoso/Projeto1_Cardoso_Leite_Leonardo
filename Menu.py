import tkinter as tk

from Classico import Classico

from Multijogador import Multijogador

from Ajuda import Ajuda

from Musica import Musica

class Menu:

    def __init__(self):
        self.window = tk.Tk()
        self.window.configure(background = 'black')
        self.window.title("Genius")
        self.window.geometry("700x700")
        
        self.window.rowconfigure(0, minsize=100, weight=1)
        self.window.rowconfigure(1, minsize=10, weight=1)
        self.window.rowconfigure(2, minsize=10, weight=1)
        self.window.rowconfigure(3, minsize=10, weight=1)
        self.window.rowconfigure(4, minsize=10, weight=1)
        self.window.rowconfigure(5, minsize=10, weight=1)
        self.window.rowconfigure(6, minsize=10, weight=1)
        
        self.window.columnconfigure(0, minsize=50, weight=1)
        self.window.columnconfigure(1, minsize=100, weight=1)
        self.window.columnconfigure(2, minsize=100, weight=1)
        self.window.columnconfigure(3, minsize=100, weight=1)
        self.window.columnconfigure(4, minsize=100, weight=1)
        self.window.columnconfigure(5, minsize=50, weight=1)
        
        self.titulo = tk.Label(self.window)
        self.titulo.grid(row=0, column=1, columnspan=4, sticky="nsew")
        self.titulo.configure(text="GENIUS BROL", fg = 'green2', background='black', font='Broadway 64')

        self.botao_classico = tk.Button(self.window)
        self.botao_classico.grid(row=1, column=1, columnspan=4, sticky="nsew")
        self.botao_classico.configure(command =lambda: self.iniciar_menu_classico(),background = 'cyan', relief = 'ridge', text="MODO CLÁSSICO", borderwidth=6, activebackground = 'green2', font='Broadway 32')
         
        self.botao_multi = tk.Button(self.window)
        self.botao_multi.grid(row=2, column=1, columnspan=4, sticky="nsew")
        self.botao_multi.configure(command =lambda: self.iniciar_menu_multijogador(),background = 'deep pink', relief = 'ridge', text="MODO MULTIJOGADOR", borderwidth=6, activebackground = 'green2', font='Broadway 32')
          
        self.botao_music = tk.Button(self.window)
        self.botao_music.grid(row=3, column=1, columnspan=4, sticky="nsew")
        self.botao_music.configure(command =lambda: self.iniciar_menu_musica(), background = 'purple1', relief = 'ridge', text="MODO MÚSICA", borderwidth=6, activebackground = 'green2', font='Broadway 32')

        self.botao_ajuda = tk.Button(self.window)
        self.botao_ajuda.grid(row=4, column=1, columnspan=4, sticky="nsew")
        self.botao_ajuda.configure(command =lambda: self.iniciar_menu_ajuda(), background = 'DarkOrange1', relief = 'ridge', text="AJUDA ?", borderwidth=6, activebackground = 'green2', font='Broadway 32')
        
    def iniciar_menu_classico(self):
        self.menu_classico = Classico()
        self.menu_classico.iniciar_classico()

    def iniciar_menu_multijogador(self):
        self.menu_multijogador = Multijogador()
        self.menu_multijogador.iniciar_multijogador()
        
    def iniciar_menu_ajuda(self):
        self.menu_ajuda = Ajuda()
        self.menu_ajuda.iniciar_ajuda()
        
    def iniciar_menu_musica(self):
        self.menu_musica = Musica()
        self.menu_musica.iniciar_musica()
  
    def iniciar_menu(self):
        self.window.mainloop() 


menu = Menu()
menu.iniciar_menu()