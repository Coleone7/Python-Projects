import pyautogui
import time
import threading
from tkinter import *

root = Tk()


class Funcs():
    auto_feed = True
    #primeiro - fazer o bot que pesca (com informações pre definidas)
        ##selecionar a vara, clicar na agua, apertar tab para selecionar inimigo, atacar, mandar o pokemon voltar na posição, clicar pra pegar o loot, repetir.
    #segundo  - fazer a função receber o botão de atalho da pesca
    #terceiro - fazer a função receber os parametros dos locais de pesca
    #quarto   - fazer a função receber a posição do local do loot
    #quinto   - fazer a função entender se existe inimigo e atacar somente quando existir inimigos
    # def Pesca_auto(self):

    #primeiro - fazer o loop de uso da comida.
    #segundo  - fazer a função usar o valor informado no campo comida_entry
    #terceiro - replicar para auto_potion

    def scan_auto_feed(self):
        if auto_feed:  #scan para verificar a situação do auto_feed
            print('ligado')

        root.after(1000, scanning) #scan de 1 sec

    def play_auto_feed(self):
        """Liga o Auto-Feed"""
        global auto_feed
        auto_feed = True

    def pause_auto_feed(self):
        """Desliga o Auto-Feed"""
        global auto_feed
        auto_feed = False





    def play_auto_potion(self):
        print('auto potion')

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets()
        root.mainloop()

    def tela(self):
        self.root.title("Auxiliar de Pesca")
        self.root.geometry("350x300")
        self.root.resizable(True, True)
        self.root.configure(background='grey')
        self.root.maxsize(width=500,height=400)
        self.root.minsize(width=300,height=200)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=1, bg='grey')
        self.frame_1.place(relx=0.01, rely=0.01, relwidth=0.99, relheight=0.99)

    def widgets(self):
        ### Botão de Pescar.
        self.bt_pescar = Button(self.frame_1, text="---------- Pescar ----------", border=2, bg='#ee1515', fg='white')
        self.bt_pescar.configure()
        self.bt_pescar.place(relx=0.1, rely=0.1, relheight=0.1, relwidth=0.8)

        ### Comida automática
        self.feed_bt = Button(self.frame_1, text="Auto Feed", command=self.play_auto_feed)
        self.feed_bt.place(relx=0.05, rely=0.3, relwidth=0.3)

        self.comida_entry = Entry(self.frame_1)
        self.comida_entry.place(relx=0.36, rely=0.3, relwidth=0.1)

        self.feed_bt_x = Button(self.frame_1, text="x", bg='black', fg= 'red', command=self.pause_auto_feed)
        self.feed_bt_x.place(relx=0.5, rely=0.3, relwidth=0.05, relheight=0.05)

        #### Poção automática
        self.potion_bt = Button(self.frame_1, text="Auto Potion", command=self.play_auto_potion)
        self.potion_bt.place(relx=0.05, rely=0.4, relwidth=0.3)

        self.potion_entry = Entry(self.frame_1)
        self.potion_entry.place(relx=0.36, rely=0.4, relwidth=0.1)

Application()
