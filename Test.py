import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


class Test(object):
    def __init__(self):
        # This creates the main window of an application
        self.window = tk.Tk()
        self.window.title("Join")
        self.window.geometry("300x300")
        self.window.configure(background='grey')

        self.path = "orc.png"

        # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        self.img = ImageTk.PhotoImage(Image.open(self.path))

        # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        self.panel = tk.Label(self.window, image=self.img)

        # The Pack geometry manager packs widgets in rows or columns.
        self.panel.pack(side="bottom", fill="both", expand="yes")

        # Start the GUI
        self.window.mainloop()

        if self.enemy.health > 0:
            if self.player.health > 0:
                if self.player.speed < self.enemy.speed:
                    print(self.enemy.name + " attacks ")
                    self.player.health -= self.enemy.attack
                    print("Player health is " + str(self.player.health))
                else:
                    print("Enemy is a(n) " + self.enemy.name)
                    t = input(" run or attack ")
                    if t == "attack":
                        self.enemy.health -= self.player.attack
                        if self.enemy.health < 0:
                            self.enemy.health = 0
                        print(self.enemy.name + " health is " + str(self.enemy.health))
                        print(self.enemy.name + " attacks")
                        self.player.health -= self.enemy.attack
                        print("Player health is " + str(self.player.health))
                        self.battle(self.player, self.enemy)
                    else:
                        return

                t = input(" run or attack ")
                if t == "attack":
                    self.enemy.health -= self.player.attack
                    if self.enemy.health < 0:
                        self.enemy.health = 0
                    print(self.enemy.name + " health is " + str(self.enemy.health))
                    self.battle(self.player, self.enemy)
                else:
                    return
            else:
                print("player dead")
                print(1 + "t")

        else:
            print("you win")
            print(self.player.name + " gained " + str(self.enemy.exp))
            self.player.exp += 20
            self.player.update()

        return


    def draw(self):
        self.root2 = tk.Tk()
        canvas = Canvas(self.root2, width=400, height=500, bg='#80c1ff')
        canvas.pack()
        img = PhotoImage(master=canvas, file='orc.png')
        img2 = PhotoImage(master=canvas, file='pokemon.png')
        button = tk.Button(canvas, text="fight", command=lambda: self.battle())
        button.place(x=200, y=200)
        canvas.create_image((50, 50), image=img, state="normal", anchor=NW)
        canvas.create_image((100, 300), image=img2, state="normal", anchor=NW)
        if self.rt2 == 2:
            return
        self.root2.mainloop()

        if self.quest.cpm == 1:
            label = tk.Label(self.root, text="Did you do it")
            label.place(x=100, y=200)
            button = tk.Button(self.root, text="yes", command=lambda: self.complete())
            button.place(x=200, y=200, width=100, relheight=100)

        else:
            label = tk.Label(self.root, text="please hurry ")
            label.place(x=100, y=200)
        if self.quest.cpm == 0:
            t = input("I need your help adventurer (y/n) ")
            if t == "y":
                print("Thanks you adventure i need you to do " + self.quest.task)
                self.quest.cpm = 1

        if self.quest.cpm == 2:
            print("thanks again")
        self.root2 = tk.Tk()
        frame = tk.Frame(self.root2, bg='#80c1ff', bd=5)
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.root2.mainloop()
        st = 1
        if st == [1, 4]:
            button = tk.Button(frame, text="Talk", command=lambda: self.talk(self.npc[0], player))
            button.place(relx=0, rely=.2, relwidth=.5, relheight=.1)

        elif st == [1, 3]:
            button = tk.Button(frame, text="Talk", command=lambda: self.talk(self.npc[1], player))
            button.place(relx=0, rely=.2, relwidth=.5, relheight=.1)

        elif st == [-1, 3]:
            button = tk.Button(frame, text="Talk", command=lambda: self.talk(self.npc[2], player))
            button.place(relx=0, rely=.2, relwidth=.5, relheight=.1)

        elif st == [1, 2]:
            button = tk.Button(frame, text="Talk", command=lambda: self.talk(self.npc[3], player))
            button.place(relx=0, rely=.2, relwidth=.5, relheight=.1)

        else:
            self.root2.destroy()

            frame = tk.Frame(self.root, bg='#80c1ff', bd=5)
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)

            button = tk.Button(frame, text="left", command=lambda: self.left(player))
            button.place(relx=0, rely=.2 * 0, relwidth=.2, relheight=.1)
            button = tk.Button(frame, text="right", command=lambda: self.right(player))
            button.place(relx=0, rely=.2 * 1, relwidth=.2, relheight=.1)
            button = tk.Button(frame, text="up", command=lambda: self.up(player))
            button.place(relx=0, rely=.2 * 2, relwidth=.2, relheight=.1)
            button = tk.Button(frame, text="down", command=lambda: self.down(player))
            button.place(relx=0, rely=.2 * 3, relwidth=.2, relheight=.1)
            button = tk.Button(frame, text="leave", command=lambda: self.leave())
            button.place(relx=0, rely=.2 * 4, relwidth=.2, relheight=.1)
            label = tk.Label(frame, text=player.quest[0])
            label.place(relx=0.5, rely=.2, relwidth=.5, relheight=.2)
    def left(self, player):
        self.pos[0] -= 1

        rand = random.randrange(0, 20)

        if rand < 21:
            self.battle(player, Enemy(player.level))
        elif rand < 21:
            print("Found Gold ")
            tr = random.randrange(0, 10)
            print(str(tr))
            player.gold += tr

    def up(self, player):
        self.pos[1] += 1

        rand = random.randrange(0, 20)

        if rand < 21:
            self.battle(player, Enemy(player.level))
        elif rand < 21:
            print("Found Gold ")
            tr = random.randrange(0, 10)
            print(str(tr))
            player.gold += tr

    def down(self, player):
        self.pos[1] -= 1

        rand = random.randrange(0, 20)

        if rand < 21:
            self.battle(player, Enemy(player.level))
        elif rand < 21:
            print("Found Gold ")
            tr = random.randrange(0, 10)
            print(str(tr))
            player.gold += tr

    def right(self, player):
        self.pos[0] += 1
        rand = random.randrange(0, 20)

        if rand < 21:
            self.battle(player, Enemy(player.level))
        elif rand < 21:
            print("Found Gold ")
            tr = random.randrange(0, 10)
            print(str(tr))
            player.gold += tr

