
import tkinter as tk

from Classico.py import *

class Menu:

    
    def __init__(self):
        self.window = tk.Tk()
        self.window.configure(background = 'green')
        self.window.title("Genius")
        self.window.geometry("700x700")
        
        self.window.rowconfigure(0, minsize=100, weight=1)
        self.window.rowconfigure(1, minsize=10, weight=1)
        self.window.rowconfigure(2, minsize=10, weight=1)
        self.window.rowconfigure(3, minsize=10, weight=1)
        self.window.rowconfigure(4, minsize=10, weight=1)
        self.window.rowconfigure(5, minsize=10, weight=1)
        
        self.window.columnconfigure(0, minsize=50, weight=1)
        self.window.columnconfigure(1, minsize=100, weight=1)
        self.window.columnconfigure(2, minsize=100, weight=1)
        self.window.columnconfigure(3, minsize=100, weight=1)
        self.window.columnconfigure(4, minsize=50, weight=1)

        
    #Criando os Botões:
        
        self.titulo = tk.Label(self.window)
        self.titulo.grid(row=0, column=1, columnspan=3, sticky="nsew")
        self.titulo.configure(text="GENIUS BROL",activebackground='black', background='green', font='Arial 67')

        self.botao_classico = tk.Button(self.window)
        self.botao_classico.grid(row=1, column=1, columnspan=3, sticky="nsew")
        self.botao_classico.configure(command =lambda: self.iniciar_menu_classico(), background = 'navy', text="Modo Clássico", font='Arial 30')
         
        self.botao_multi = tk.Button(self.window)
        self.botao_multi.grid(row=2, column=1, columnspan=3, sticky="nsew")
        self.botao_multi.configure(background = 'deep pink', text="Modo Multijogador", font='Arial 30')
          
        self.botao_music = tk.Button(self.window)
        self.botao_music.grid(row=3, column=1, columnspan=3, sticky="nsew")
        self.botao_music.configure(background = 'purple1', text="Modo Música", font='Arial 30')

        self.botao_ajuda = tk.Button(self.window)
        self.botao_ajuda.grid(row=4, column=1, columnspan=3, sticky="nsew")
        self.botao_ajuda.configure(background = 'DarkOrange1', text="? Ajuda ?", font='Arial 30')
        
    def iniciar_menu_classico(self):
        self.menu_classico = Classico()
        self.menu_classico.iniciar_classico()
        
    def iniciar_menu(self):
        self.window.mainloop() 

menu =Menu()
menu.iniciar_menu()