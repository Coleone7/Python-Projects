from tkinter import *
import threading
import time


should_run = False
class a:
    def __init__(self):
        while True:
            if should_run:
                for i in range(10):
                    if not should_run:
                        print('Stopped...')
                        break
                    if should_run:
                        time.sleep(0.5)
                        print(i)

t1 = threading.Thread(target=a,daemon=True)
t1.start()

class gui:

    def __init__(self, window):

        # play button
        self.play_frame = Frame(master=window, relief=FLAT, borderwidth=1)
        self.play_frame.grid(row=0, column=0, padx=1, pady=1)
        self.play_button = Button(self.play_frame, text="play", fg="blue", command=lambda: self.play(True))
        self.play_button.pack()
        # stop button
        self.stop_frame = Frame(master=window, relief=FLAT, borderwidth=1)
        self.stop_frame.grid(row=0, column=2, padx=1, pady=1)
        self.stop_button = Button(self.stop_frame, text="stop", fg="red", command=lambda: self.play(False))
        self.stop_button.pack()


    def play(self, switch):
        global should_run
        should_run = switch



root = Tk()

app = gui(root)
root.mainloop()