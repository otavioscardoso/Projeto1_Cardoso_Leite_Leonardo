import tkinter as tk

class Multijogador:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Modo multijogador")
        self.window.geometry("2000x2000")
        self.window.configure(background = 'deep pink')
        self.window.rowconfigure(0, minsize=10, weight=1)
        self.window.rowconfigure(1, minsize=10, weight=1)
        self.window.rowconfigure(2, minsize=10, weight=1)
        self.window.rowconfigure(3, minsize=10, weight=1)
        self.window.rowconfigure(4, minsize=10, weight=1)
        self.window.rowconfigure(5, minsize=10, weight=1)
        self.window.rowconfigure(6, minsize=10, weight=1)
        self.window.rowconfigure(7, minsize=10, weight=1)
        
        
        
        

        self.window.columnconfigure(0, minsize=100, weight=1)
        self.window.columnconfigure(1, minsize=100, weight=1)
        self.window.columnconfigure(2, minsize=100, weight=1)
        self.window.columnconfigure(3, minsize=100, weight=1)
        self.window.columnconfigure(4, minsize=100, weight=1)
        self.window.columnconfigure(5, minsize=100, weight=1)
        self.window.columnconfigure(6, minsize=100, weight=1)
        self.window.columnconfigure(7, minsize=100, weight=1)
        self.window.columnconfigure(8, minsize=100, weight=1)
        self.window.columnconfigure(9, minsize=100, weight=1)
        self.window.columnconfigure(10, minsize=100, weight=1)
        
        

        self.pontos = tk.Label(self.window)
        self.pontos.grid(row=1, column=3, columnspan=2, sticky="nsew")
        self.pontos.configure(text="Pontos 1:", font='Symbol 30', background='snow')
        
        self.pontos = tk.Label(self.window)
        self.pontos.grid(row=1, column=8, columnspan=2, sticky="nsew")
        self.pontos.configure(text="Pontos 2:", font='Symbol 30', background='snow')
        
        self.jogador1 = tk.Label(self.window)
        self.jogador1.grid(row=1, column=1, columnspan=2, sticky="nsew")
        self.jogador1.configure(text="Jogador1:", font='Symbol 30', background='snow')
        
        self.jogador2 = tk.Label(self.window)
        self.jogador2.grid(row=1, column=6, columnspan=2, sticky="nsew")
        self.jogador2.configure(text="Jogador2:", font='Symbol 30', background='snow')
        
        self.titulo = tk.Label(self.window)
        self.titulo.grid(row=0, column=4, columnspan=4, sticky="nsew")
        self.titulo.configure(text="Multijogador", font='Symbol 70', background='deep pink')

        self.botão0 = tk.Button(self.window)
        self.botão0.grid(row=2, column=1, columnspan=2, rowspan=2, sticky="nsew")
        self.botão0.configure(background = 'yellow')
         
        self.botão1 = tk.Button(self.window)
        self.botão1.grid(row=4, column=1, columnspan=2, rowspan=2, sticky="nsew")
        self.botão1.configure(background = 'green2')
          
        self.botão2 = tk.Button(self.window)
        self.botão2.grid(row=2, column=3, columnspan=2, rowspan=2, sticky="nsew")
        self.botão2.configure(background = 'red')

        self.botão3 = tk.Button(self.window)
        self.botão3.grid(row=4, column=3, columnspan=2, rowspan=2, sticky="nsew")
        self.botão3.configure(background = 'blue')
        
        
        self.botão4 = tk.Button(self.window)
        self.botão4.grid(row=2, column=6, columnspan=2, rowspan=2, sticky="nsew")
        self.botão4.configure(background = 'yellow')
         
        self.botão5 = tk.Button(self.window)
        self.botão5.grid(row=4, column=6, columnspan=2, rowspan=2, sticky="nsew")
        self.botão5.configure(background = 'green2')
          
        self.botão6 = tk.Button(self.window)
        self.botão6.grid(row=2, column=8, columnspan=2, rowspan=2, sticky="nsew")
        self.botão6.configure(background = 'red')

        self.botão7 = tk.Button(self.window)
        self.botão7.grid(row=4, column=8, columnspan=2, rowspan=2, sticky="nsew")
        self.botão7.configure(background = 'blue')
        
        self.botãoiniciar = tk.Button(self.window)
        self.botãoiniciar.grid(row=7, column=0, sticky="nsew")
        self.botãoiniciar.configure(text="Iniciar", font='Symbol 30')
          

        self.botãomenu = tk.Button(self.window)
        self.botãomenu.grid(row=7, column=1, sticky="nsew")
        self.botãomenu.configure(text="Menu", font='Symbol 30')
  
    def iniciar(self):
        self.window.mainloop() 

projeto = Multijogador()
projeto.iniciar()
        