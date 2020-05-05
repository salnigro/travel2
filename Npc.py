from Quest import Quest
import tkinter as tk


class Npc(object):
    def __init__(self):
        self.quest = Quest()
        self.t = 0

    def speech(self, player):
        self.root = tk.Tk()
        frame = tk.Frame(self.root, bg='#80c1ff', bd=5)
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        if self.quest.cpm == 0:
            label = tk.Label(frame, text="I need your help adventurer", bg='#80c1ff')
            label.place(relx=0, rely=0, relwidth=1, relheight=.2)
            button = tk.Button(frame, text="yes", command=lambda: self.give(player))
            button.place(relx=0, rely=.2, relwidth=.5, relheight=.1)
            button = tk.Button(frame, text="no", command=lambda: self.ngive())
            button.place(relx=.5, rely=.2, relwidth=.5, relheight=.1)
        if self.quest.cpm == 1:
            label = tk.Label(frame, text="Did you do it", bg='#80c1ff')
            label.place(relx=.3, rely=0, relwidth=.4, relheight=.2)
            button = tk.Button(frame, text="yes", command=lambda: self.complete(player))
            button.place(relx=0, rely=.2, relwidth=.5, relheight=.1)
            button = tk.Button(frame, text="no", command=lambda: self.ncomp())
            button.place(relx=.5, rely=.2, relwidth=.5, relheight=.1)
        if self.quest.cpm == 2:
            label = tk.Label(frame, text="Thank you", bg='#80c1ff')
            label.place(relx=.3, rely=0, relwidth=.4, relheight=.2)
            button = tk.Button(frame, text="Go Back", command=lambda: self.gobck())
            button.place(relx=.25, rely=.2, relwidth=.5, relheight=.1)
        self.root.mainloop()

    def complete(self, player):
        frame = tk.Frame(self.root, bg='#80c1ff', bd=5)
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        for i in range(len(player.quest)):
            if self.quest.task == player.quest[i]:
                if player.counter[i] >= 10:
                    frame = tk.Frame(self.root, bg='#80c1ff', bd=5)
                    frame.place(relx=0, rely=0, relwidth=1, relheight=1)
                    label = tk.Label(frame, text="Thank you", bg='#80c1ff')
                    label.place(relx=.3, rely=0, relwidth=.4, relheight=.2)
                    player.quest.pop(i)
                    player.counter.pop(i)
                    button = tk.Button(frame, text="Go Back", command=lambda: self.gobck())
                    button.place(relx=.25, rely=.2, relwidth=.5, relheight=.1)
                else:
                    frame = tk.Frame(self.root, bg='#80c1ff', bd=5)
                    frame.place(relx=0, rely=0, relwidth=1, relheight=1)
                    print(player.counter[i])
                    label = tk.Label(frame, text="No you didn't", bg='#80c1ff')
                    label.place(relx=.3, rely=0, relwidth=.4, relheight=.2)
                    button = tk.Button(frame, text="Go Back", command=lambda: self.gobck())
                    button.place(relx=.25, rely=.2, relwidth=.5, relheight=.1)
        self.quest.cpm = 2

    def ncomp(self):
        frame = tk.Frame(self.root, bg='#80c1ff', bd=5)
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        label = tk.Label(self.root, text="please hurry ", bg='#80c1ff')
        label.place(relx=.3, rely=0, relwidth=.4, relheight=.2)
        button = tk.Button(frame, text="Go Back", command=lambda: self.gobck())
        button.place(relx=.25, rely=.2, relwidth=.5, relheight=.1)

    def gobck(self):
        self.root.destroy()

    def give(self, player):
        player.quest.append(self.quest.task)
        player.counter.append(0)
        frame = tk.Frame(self.root, bg='#80c1ff', bd=5)
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        label = tk.Label(self.root, text=self.quest.task, bg='#80c1ff')
        label.place(relx=0, rely=0, relwidth=1, relheight=.2)
        button = tk.Button(frame, text="Go Back", command=lambda: self.gobck())
        button.place(relx=.25, rely=.2, relwidth=.5, relheight=.1)
        self.quest.cpm = 1

    def ngive(self):
        frame = tk.Frame(self.root, bg='#80c1ff', bd=5)
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        label = tk.Label(self.root, text="Oh well", bg='#80c1ff')
        label.place(relx=0, rely=0, relwidth=1, relheight=.2)
        button = tk.Button(frame, text="Go Back", command=lambda: self.gobck())
        button.place(relx=.25, rely=.2, relwidth=.5, relheight=.1)