from tkinter import *

class Check_box:

    def __init__(self, master):

        self.state = 0
        self.canvas = Canvas(master)

        self.canvas.bind("<Button-1>", self.state_changer)

    def state_changer(self, event):

        self.canvas.delete("all")
        self.state += 1

        if self.state == 3:
            self.state = 0

        self.canvas.create_rectangle(0, 0, 10, 10*self.state)
