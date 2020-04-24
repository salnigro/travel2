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
