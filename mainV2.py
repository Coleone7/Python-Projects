import pyautogui, time
from tkinter import *

auto_feed = False #flag global auto_feed
auto_pesca = False #flag global auto_pesca
auto_potion = False #flag global auto_potion

lock_pk_x = 0
lock_pk_y = 0
lock_loot1x = 0
lock_loot1y = 0
lock_loot2x = 0
lock_loot2y = 0
lock_loot3x = 0
lock_loot3y = 0
lock_agua_x = 0
lock_agua_y = 0
# -- Auto-Pesca -- ###################################################

def scan_auto_pesca():
    """Roda o auto pesca"""
    if auto_pesca:
        time.sleep(2)
        pyautogui.press(pesca_entry.get())
        time.sleep(0.5)
        pyautogui.click(x=lock_agua_x, y=lock_agua_y)

    root.after(32000, scan_auto_pesca) #scan de 1 sec


def play_auto_pesca():
    """Liga a auto pesca"""
    global auto_pesca
    auto_pesca = True
    print("auto pesca ligado")
    #clicar na aguá com o atalho da vara.
    #
def pause_auto_pesca():
    """Desliga a auto pesca"""
    global auto_pesca
    auto_pesca = False
    print("auto pesca desligado")

# -- Auto Atack -- ##################################################
#def auto_atack():
    #scan no local do battle.
    #se tiver pokemon, click no pokemon -> soltar atacks
    #quando sumir o pokemon -> rodar auto_loot()
    #recomeçar o scan.

def play_auto_atack():
    """Liga o Auto-Atack"""
    global auto_pesca
    auto_pesca = True
    print('play auto atack')

def pause_auto_atack():
    """Desliga o Auto-Atack"""
    global auto_pesca
    auto_pesca = False
    print('auto atack desligado')

# -- Auto-loot / Retorno de posição pokemon# -- ######################

def auto_loot():
    """Right-click na posição dos tês lock_loot e middle-click na posição do lock_pokemon"""

    pyautogui.position(lock_pk_x, lock_pk_y)
    time.sleep(0.5)
    pyautogui.position(lock_loot1x, lock_loot1y)
    time.sleep(0.5)
    pyautogui.position(lock_loot2x, lock_loot2y)
    time.sleep(0.5)
    pyautogui.position(lock_loot3x, lock_loot3y)

# -- Lock pokemon -- ##############################################

def lock_pokemon():
    """Guarda as informações da posição da tela em que o pokemon irá ficar fixo"""
    global lock_pk_x, lock_pk_y
    time.sleep(1.5)
    lock_pk_x, lock_pk_y = pyautogui.position()
    print(lock_pk_x, lock_pk_y)

# -- Lock agua -- #################################################

def lock_agua():
    """Guarda as informações da posição da agua que irá ser usado a vara"""
    global lock_agua_x, lock_agua_y
    time.sleep(1.5)
    lock_agua_x, lock_agua_y = pyautogui.position()
    print(lock_agua_x, lock_agua_y)


# -- Lock loot -- ################################################

def lock_loot1():
    """Guarda as informações da primeira posição de loot"""
    global lock_loot1x, lock_loot1y
    time.sleep(1.5)
    lock_loot1x, lock_loot1y = pyautogui.position()
    print(lock_loot1x, lock_loot1y)

def lock_loot2():
    """Guarda as informações da segunda posição de loot"""
    global lock_loot2x, lock_loot2y
    time.sleep(1.5)
    lock_loot2x, lock_loot2y = pyautogui.position()
    print(lock_loot2x, lock_loot2y)


def lock_loot3():
    """Guarda as informações da terceira posição de loot"""
    global lock_loot3x, lock_loot3y
    time.sleep(1.5)
    lock_loot3x, lock_loot3y = pyautogui.position()
    print(lock_loot3x, lock_loot3y)

# -- autofeed -- ###################################################
def scan_auto_feed():
    """Roda o auto feed"""
    if auto_feed:
            #time.sleep(1)
            pyautogui.press(comida_entry.get())

    root.after(1000, scan_auto_feed) #scan de 1 sec

def play_auto_feed():
    """Liga o Auto-Feed"""
    global auto_feed
    auto_feed = True

def pause_auto_feed():
    """Desliga o Auto-Feed"""
    global auto_feed
    auto_feed = False


# -- auto_potion -- ##################################################

def scan_auto_pesca():
    """Roda o auto_potion"""
    if auto_potion:
        print("rodando")


    root.after(1000, scan_auto_pesca)  # scan de 1 sec

def play_auto_potion():
    """Liga o Auto-Potion"""
    global auto_potion
    auto_potion = True
    print('play auto potion')

def pause_auto_potion():
    """Desliga o Auto-Potion"""
    global auto_potion
    auto_potion = False
    print('pause auto potion')

# -- STOP ALL -- #####################################################
def stop_all():
    """Desliga todas as globais"""
    print('PARADA')
    global auto_feed,auto_pesca, auto_potion
    auto_feed = False  # flag global auto_feed
    auto_pesca = False  # flag global auto_pesca
    auto_potion = False #flag global auto_potion


########################################################################################################################
root = Tk()

#tela()
root.title("Auxiliar de Pesca")
root.geometry("350x300")
root.resizable(True, True)
root.configure(background='grey')
root.maxsize(width=500,height=400)
root.minsize(width=350,height=300)

#frames_da_tela()
frame_1 = Frame(root, bd=1, bg='grey')
frame_1.place(relx=0.01, rely=0.01, relwidth=0.99, relheight=0.99)

#widgets()
### Função de Pesca
pesca_bt = Button(frame_1, text="---------- Pescar ----------", border=2, bg='#ee1515', fg='white',command=play_auto_pesca)
pesca_bt.configure()
pesca_bt.place(relx=0.1, rely=0.1, relheight=0.1, relwidth=0.73)

pesca_bt_x = Button(frame_1, text="x", bg='black', fg= 'red', command=pause_auto_pesca)
pesca_bt_x.place(relx=0.85, rely=0.12, relwidth=0.05, relheight=0.05)

pesca_label_atalho = Label(frame_1, text="Atalho Vara")
pesca_label_atalho.place(relx=0.05, rely=0.25)

pesca_entry = Entry(frame_1)
pesca_entry.place(relx=0.26, rely=0.25, relwidth=0.1)

pesca_bt_pk_position = Button(frame_1, text="Lock Pokemon", command=lock_pokemon)
pesca_bt_pk_position.place(relx=0.4, rely=0.25, relwidth=0.26)

pesca_bt_agua_position = Button(frame_1, text="Lock Agua", command= lock_agua)
pesca_bt_agua_position.place(relx=0.4, rely=0.35, relwidth=0.26)

loot_bt_1 = Button(frame_1, text="Lock loot 1", command=lock_loot1)
loot_bt_1.place(relx=0.7, rely=0.25)

loot_bt_2 = Button(frame_1, text="Lock loot 2", command=lock_loot2)
loot_bt_2.place(relx=0.7, rely=0.35)

loot_bt_3 = Button(frame_1, text="Lock loot 3", command=lock_loot3)
loot_bt_3.place(relx=0.7, rely=0.45)

### Auto Atack

auto_atack = Button(frame_1, text="---- Auto Atack ----", command=play_auto_atack, bg="#2237B4", fg='white')
auto_atack.place(relx=0.05, rely=0.45, relheight=0.1, relwidth=0.6)

auto_atack_x = Button(frame_1, text="x", bg='black', fg='#2237B4', command=pause_auto_atack)
auto_atack_x.place(relx=0.3, rely=0.55, relwidth=0.05, relheight=0.05)

### Comida automática
feed_bt = Button(frame_1, text="Auto Feed", command=play_auto_feed)
feed_bt.place(relx=0.05, rely=0.7, relwidth=0.3)

comida_entry = Entry(frame_1)
comida_entry.place(relx=0.36, rely=0.7, relwidth=0.1)

feed_bt_x = Button(frame_1, text="x", bg='black', fg= 'red', command=pause_auto_feed)
feed_bt_x.place(relx=0.5, rely=0.7, relwidth=0.05, relheight=0.05)

#### Poção automática
potion_bt = Button(frame_1, text="Auto Potion", command=play_auto_potion)
potion_bt.place(relx=0.05, rely=0.8, relwidth=0.3)

potion_entry = Entry(frame_1)
potion_entry.place(relx=0.36, rely=0.8, relwidth=0.1)

potion_bt_x = Button(frame_1, text="x", bg='black', fg= 'red', command=pause_auto_potion)
potion_bt_x.place(relx=0.5, rely=0.8, relwidth=0.05, relheight=0.05)

#### STOP

stop_bt = Button(frame_1, text= 'STOP', bg='red', fg='white', command= stop_all)
stop_bt.place(relx=0.9, rely=0.9,)


root.after(1000, scan_auto_feed)
root.after(1000, scan_auto_pesca)

root.mainloop()
















