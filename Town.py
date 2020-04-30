from Npc import Npc
from Road import Road
import tkinter as tk


class Town(object):
    def __init__(self, npc, name, location):
        self.leave = 0
        self.array = []
        self.npc = npc
        self.name = name
        self.location = location
        self.roads = [
            Road("0 rd", [0, 0], 0),
            Road("1 rd", [0, 1], 0),
            Road("2 rd", [0, 2], 0),
            Road("3 rd", [0, 3], 0),
            Road("4 rd", [0, 4], 0),
            Road("5 rd", [1, 4], 0),
            Road("6 rd", [1, 3], 0),
            Road("7 rd", [-1, 3], 0),
            Road("8 rd", [-1, 1], 0),
            Road("9 rd", [1, 2], 0),
        ]

        self.roadp = [
            Road("0 rd", [0, 0], [0, 1]),
            Road("0 rd", [0, 0], [0, 2]),
            Road("0 rd", [0, 0], [0, 3]),
            Road("0 rd", [0, 0], [0, 4]),
            Road("1 rd", [0, 1], [0, 0]),
            Road("1 rd", [0, 1], [0, 2]),
            Road("1 rd", [0, 1], [0, 3]),
            Road("1 rd", [0, 1], [0, 4]),
            Road("1 rd", [0, 1], [-1, 1]),
            Road("2 rd", [0, 2], [0, 0]),
            Road("2 rd", [0, 2], [0, 1]),
            Road("2 rd", [0, 2], [0, 3]),
            Road("2 rd", [0, 2], [0, 4]),
            Road("2 rd", [0, 2], [1, 2]),
            Road("3 rd", [0, 3], [0, 0]),
            Road("3 rd", [0, 3], [0, 1]),
            Road("3 rd", [0, 3], [0, 2]),
            Road("3 rd", [0, 3], [0, 4]),
            Road("3 rd", [0, 3], [-1, 3]),
            Road("4 rd", [0, 4], [0, 0]),
            Road("4 rd", [0, 4], [0, 1]),
            Road("4 rd", [0, 4], [0, 2]),
            Road("4 rd", [0, 4], [0, 3]),
            Road("4 rd", [0, 4], [1, 4]),
            Road("5 rd", [1, 4], [0, 4]),
            Road("5 rd", [1, 4], [1, 3]),
            Road("6 rd", [1, 3], [1, 4]),
            Road("7 rd", [-1, 3], [0, 3]),
            Road("7 rd", [-1, 3], [-1, 1]),
            Road("8 rd", [-1, 1], [-1, 3]),
            Road("8 rd", [-1, 1], [0, 1]),
            Road("9 rd", [1, 2], [0, 2]),
        ]

    # Road("9 rd",[1,2],[2,2]),Road("10 rd",[2,0],[2,2])

    def menu(self, st, player):
        self.array = []
        self.root = tk.Tk()
        self.root.geometry("600x600")
        for i in range(0, len(self.roadp)):
            if st == self.roadp[i].start:
                for j in range(len(self.roadp)):
                    if (self.roadp[i].start == self.roadp[j].end) & (self.roadp[i].end == self.roadp[j].start):
                        s = self.roadp[j].name
                        s = s[0:1]
                        s = int(s)
                        self.array.append(self.roads[s])
                        break
        self.frame = tk.Frame(self.root, bg='#80c1ff', bd=5)
        self.frame.place(relx=0, rely=0, width=700, height=900)
        canvas = tk.Canvas(self.frame, width=700, height=900, bg='#80c1ff')
        canvas.create_line(300, 100, 300, 500, fill='blue', width=5)
        canvas.create_line(300, 400, 100, 400, fill='blue', width=5)
        canvas.create_line(100, 400, 100, 200, fill='blue', width=5)
        canvas.create_line(100, 200, 300, 200, fill='blue', width=5)
        canvas.create_line(300, 300, 500, 300, fill='blue', width=5)
        canvas.create_line(300, 100, 500, 100, fill='blue', width=5)
        canvas.create_line(500, 100, 500, 200, fill='blue', width=5)
        canvas.pack()
        self.layout(player)
        button = tk.Button(self.frame, text="leave", command=lambda: self.leaves())
        button.place(relx=0, rely=.1 * 8, relwidth=.05, relheight=.01)
        if self.leave == 1:
            return
        self.root.mainloop()

    def leaves(self):
        self.root.destroy()
        self.leave = 1

    def road(self, name, player):
        for i in range(len(self.roads)):
            if name == self.roads[i].name:
                st = self.roads[int(i)].start
                self.root.destroy()
        self.root2 = tk.Tk()
        frame = tk.Frame(self.root2, bg='#80c1ff', bd=5)
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        if st == [1, 4]:
            button = tk.Button(frame, text="Talk", command=lambda: self.talk(self.npc[0], player))
            button.place(relx=0, rely=.2, relwidth=.5, relheight=.1)
            button = tk.Button(frame, text="Continue", command=lambda: self.cont())
            button.place(relx=0, rely=.4, relwidth=.5, relheight=.1)

        elif st == [1, 3]:
            button = tk.Button(frame, text="Talk", command=lambda: self.talk(self.npc[1], player))
            button.place(relx=0, rely=.2, relwidth=.5, relheight=.1)
            button = tk.Button(frame, text="Continue", command=lambda: self.cont())
            button.place(relx=0, rely=.4, relwidth=.5, relheight=.1)

        elif st == [-1, 3]:
            button = tk.Button(frame, text="Talk", command=lambda: self.talk(self.npc[2], player))
            button.place(relx=0, rely=.2, relwidth=.5, relheight=.1)
            button = tk.Button(frame, text="Continue", command=lambda: self.cont())
            button.place(relx=0, rely=.4, relwidth=.5, relheight=.1)

        elif st == [1, 2]:
            button = tk.Button(frame, text="Talk", command=lambda: self.talk(self.npc[3], player))
            button.place(relx=0, rely=.2, relwidth=.5, relheight=.1)
            button = tk.Button(frame, text="Continue", command=lambda: self.cont())
            button.place(relx=0, rely=.4, relwidth=.5, relheight=.1)

        else:
            self.root2.destroy()
        self.menu(st, player)

    def talk(self, npc, player):
        self.root2.destroy()

        npc.speech(player)
        return

    def cont(self):
        self.root2.destroy()

    def layout(self, player):
        for i in range(len(self.array)):
            if self.array[i] == self.roads[0]:
                button = tk.Button(self.frame, bg='#e68e8e', text=self.roads[0].name,
                                   command=lambda: self.road(self.roads[0].name, player))
                button.place(x=300 - 200 * self.roads[0].start[0], y=500 - 100 * self.roads[0].start[1], relwidth=.05,
                             relheight=.05)
            if self.array[i] == self.roads[1]:
                button = tk.Button(self.frame, bg='#e68e8e', text=self.roads[1].name,
                                   command=lambda: self.road(self.roads[1].name, player))
                button.place(x=300 - 200 * self.roads[1].start[0], y=500 - 100 * self.roads[1].start[1], relwidth=.05,
                             relheight=.05)
            if self.array[i] == self.roads[2]:
                button = tk.Button(self.frame, bg='#e68e8e', text=self.roads[2].name,
                                   command=lambda: self.road(self.roads[2].name, player))
                button.place(x=300 - 200 * self.roads[2].start[0], y=500 - 100 * self.roads[2].start[1], relwidth=.05,
                             relheight=.05)
            if self.array[i] == self.roads[3]:
                button = tk.Button(self.frame, bg='#e68e8e', text=self.roads[3].name,
                                   command=lambda: self.road(self.roads[3].name, player))
                button.place(x=300 - 200 * self.roads[3].start[0], y=500 - 100 * self.roads[3].start[1], relwidth=.05,
                             relheight=.05)
            if self.array[i] == self.roads[4]:
                button = tk.Button(self.frame, bg='#e68e8e', text=self.roads[4].name,
                                   command=lambda: self.road(self.roads[4].name, player))
                button.place(x=300 - 200 * self.roads[4].start[0], y=500 - 100 * self.roads[4].start[1], relwidth=.05,
                             relheight=.05)
            if self.array[i] == self.roads[5]:
                button = tk.Button(self.frame, bg='#e68e8e', text=self.roads[5].name,
                                   command=lambda: self.road(self.roads[5].name, player))
                button.place(x=300 + 200 * self.roads[5].start[0], y=500 - 100 * self.roads[5].start[1], relwidth=.05,
                             relheight=.05)
            if self.array[i] == self.roads[6]:
                button = tk.Button(self.frame, bg='#e68e8e', text=self.roads[6].name,
                                   command=lambda: self.road(self.roads[6].name, player))
                button.place(x=300 + 200 * self.roads[6].start[0], y=500 - 100 * self.roads[6].start[1], relwidth=.05,
                             relheight=.05)
            if self.array[i] == self.roads[7]:
                button = tk.Button(self.frame, bg='#e68e8e', text=self.roads[7].name,
                                   command=lambda: self.road(self.roads[7].name, player))
                button.place(x=300 + 200 * self.roads[7].start[0], y=500 - 100 * self.roads[7].start[1], relwidth=.05,
                             relheight=.05)
            if self.array[i] == self.roads[8]:
                button = tk.Button(self.frame, bg='#e68e8e', text=self.roads[8].name,
                                   command=lambda: self.road(self.roads[8].name, player))
                button.place(x=300 + 200 * self.roads[8].start[0], y=500 - 100 * self.roads[8].start[1], relwidth=.05,
                             relheight=.05)
            if self.array[i] == self.roads[9]:
                button = tk.Button(self.frame, bg='#e68e8e', text=self.roads[9].name,
                                   command=lambda: self.road(self.roads[9].name, player))
                button.place(x=500, y=300, relwidth=.05,
                             relheight=.05)
        button = tk.Button(self.frame, bg='#e68e8e', text="leave",
                           command=lambda: self.leaves())
        button.place(x=100, y=100, relwidth=.05,
                     relheight=.05)