import tkinter as tk

class Ajuda:
    def __init__(self):
        self.window_ajuda = tk.Tk()
        self.window_ajuda.config(background = 'black')
        self.window_ajuda.title("Ajuda")
        self.window_ajuda.geometry("700x700")
        
        self.window_ajuda.rowconfigure(0, minsize=10, weight=1)
        self.window_ajuda.rowconfigure(1, minsize=10, weight=1)
        self.window_ajuda.rowconfigure(2, minsize=10, weight=1)
        self.window_ajuda.rowconfigure(3, minsize=10, weight=1)
        self.window_ajuda.rowconfigure(4, minsize=10, weight=1)
        self.window_ajuda.rowconfigure(5, minsize=10, weight=1)
        self.window_ajuda.rowconfigure(6, minsize=10, weight=1)
        
        self.window_ajuda.columnconfigure(0, minsize=50, weight=1)
        self.window_ajuda.columnconfigure(1, minsize=100, weight=1)
        self.window_ajuda.columnconfigure(2, minsize=100, weight=1)
        self.window_ajuda.columnconfigure(3, minsize=100, weight=1)
        self.window_ajuda.columnconfigure(4, minsize=100, weight=1) 
        self.window_ajuda.columnconfigure(5, minsize=50, weight=1)
        
        self.voltar = tk.Button(self.window_ajuda)
        self.voltar.grid(row=5, column=0, rowspan=2, columnspan=2, sticky="nsew")
        self.voltar.configure(text="MENU", font='Broadway 16', fg = "DarkOrange1", background = "black", activebackground = 'green2', relief = 'ridge', borderwidth=6)
        
        self.regras = tk.Label(self.window_ajuda)
        self.regras.grid(row=2, column=0, columnspan=6, sticky="nsew")
        self.regras.configure(text = 'Modo Simples:\n\
        Neste tipo do jogo o Genius fará uma sequência e o objetivo do usuário é conseguir\n\
        memorizá-la e repeti-la. Tal sequência inicia com apenas um botão a ser apertado\n\
        e continua aumentando de um em um até que o usuário a erre. O nível atingido pelo\n\
        usuário é igual ao número de elementos da sequência que\n\ele conseguiu memorizar.\n\n\n\
        Modo Multijogador: \n\
        Este modo faz com que dois jogadores possam jogar ao mesmo tempo. A dinâmica deste\n\
        jogo funciona da seguinte forma: o primeiro jogador ecolhe um botão para iniciar o\n\
        jogo. Em seguida, o segundo jogador deverá apertar o primeiro botão e adicionar\n\
        mais um a sua escolha. Quando a vez volta ao primeiro jogador, ele deverá apertar\n\
        o seu botão, o botão escolhido pelo segundo jogador e mais um a sua escolha. E\n\
        assim o jogo continua sucessivamente até algum dos doiserrar a sequência.\n\n\n\
        Modo Música: \n\
        Neste modo, o jogo irá funcionar assim como o modo clássico, a única diferença é\n\
        que conforme os niveis vão aumentando, o tempo de duração de determinada música que\n\
        está tocando de fundo também aumentará. Desta maneira, será cada vez mais fácil\n\
        para o jogador detectar qual música está tocando. Durante todo o jogo o usuário\n\
        conseguirá escolher uma musica entre quatro alternativas mostradas na tela. Assim,\n\
        quanto mais rápido o jogador acertar a música que está tocando mais pontos ganhará.', fg = 'DarkOrange1', font='Broadway 10', background='black')
        
        self.titulo = tk.Label(self.window_ajuda)
        self.titulo.grid(row=0, column=1, columnspan = 4, sticky="nsew")
        self.titulo.configure(text = 'AJUDA', fg = 'DarkOrange1', font='Broadway 64', background='black')
        
    def iniciar_ajuda(self):
        self.window_ajuda.mainloop() 
        
