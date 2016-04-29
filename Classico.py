import tkinter as tk

class Classico:
    def __init__(self):
        self.window_classico = tk.Tk()
        self.window_classico.config(background = 'navy')
        self.window_classico.title("Modo clássico")
        self.window_classico.geometry("700x700")
        
        self.window_classico.rowconfigure(0, minsize=10, weight=1)
        self.window_classico.rowconfigure(1, minsize=10, weight=1)
        self.window_classico.rowconfigure(2, minsize=10, weight=1)
        self.window_classico.rowconfigure(3, minsize=10, weight=1)
        self.window_classico.rowconfigure(4, minsize=10, weight=1)
        self.window_classico.rowconfigure(5, minsize=10, weight=1)
        self.window_classico.rowconfigure(6, minsize=10, weight=1)
        
        self.window_classico.columnconfigure(0, minsize=100, weight=1)
        self.window_classico.columnconfigure(1, minsize=100, weight=1)
        self.window_classico.columnconfigure(2, minsize=100, weight=1)
        self.window_classico.columnconfigure(3, minsize=100, weight=1)
        self.window_classico.columnconfigure(4, minsize=100, weight=1)
        self.window_classico.columnconfigure(5, minsize=100, weight=1)

        self.pontos = tk.Label(self.window_classico)
        self.pontos.grid(row=6, column=3, columnspan=3, sticky="nsew")
        self.pontos.configure(text="Pontos:", font='Arial 20', background='snow')
        
        self.titulo = tk.Label(self.window_classico)
        self.titulo.grid(row=0, column=1, columnspan=4, sticky="nsew")
        self.titulo.configure(text = 'Clássico', fg = 'snow', font='Arial 67', background='navy')

        self.botão1 = tk.Button(self.window_classico)
        self.botão1.grid(row=1, column=1, columnspan=2, rowspan=2, sticky="nsew")
        self.botão1.configure(background = 'yellow')
         
        self.botão2 = tk.Button(self.window_classico)
        self.botão2.grid(row=3, column=1, columnspan=2, rowspan=2, sticky="nsew")
        self.botão2.configure(background = 'green2')
          
        self.botão3 = tk.Button(self.window_classico)
        self.botão3.grid(row=1, column=3, columnspan=2, rowspan=2, sticky="nsew")
        self.botão3.configure(background = 'red')

        self.botão4 = tk.Button(self.window_classico)
        self.botão4.grid(row=3, column=3, columnspan=2, rowspan=2, sticky="nsew")
        self.botão4.configure(background = 'blue')
        
        self.botãoiniciar = tk.Button(self.window_classico)
        self.botãoiniciar.grid(row=6, column=0, sticky="nsew")
        self.botãoiniciar.configure(background = 'snow', text="Iniciar", font='Arial 20')
          
        self.botãopausar = tk.Button(self.window_classico)
        self.botãopausar.grid(row=6, column=1,sticky="nsew")
        self.botãopausar.configure(background = 'snow', text="Pausar", font='Arial 20')

        self.botãomenu = tk.Button(self.window_classico)
        self.botãomenu.grid(row=6, column=2, sticky="nsew")
        self.botãomenu.configure(background = 'snow', text="Menu", font='Arial 20')
        
    def quit(self):
        self.window.destroy()
  
    def iniciar_classico(self):
        self.window_classico.mainloop() 

