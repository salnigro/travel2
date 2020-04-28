from Quest import Quest
import tkinter as tk


class Npc(object):
    def __init__(self):
        self.quest = Quest()

    def speech(self):
        self.root = tk.Tk()
        frame = tk.Frame(self.root, bg='#80c1ff', bd=5)
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        if self.quest.cpm == 1:
            label = tk.Label(frame, text="Did you do it")
            label.place(x=100, y=200)
            button = tk.Button(frame, text="yes", command=lambda: self.complete())
            button.place(relx=0, rely=.1 * 8, relwidth=.5, relheight=.1)
        self.root.mainloop()

    def complete(self):
        self.quest.cpm = 2
