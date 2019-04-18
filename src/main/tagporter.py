from tkinter import *
from tkinter.filedialog import askopenfilename

class Tag_porter:

    def __init__(self, master):

        self.canvas = Canvas(master,width=10, height=10)

        self.canvas.bind("<Button-1>", self.file_picker)


        self.canvas.create_rectangle(1, 1, 10, 10, fill="Blue")

    def file_picker(self, event):

        self.filename = askopenfilename()
        print(self.filename)
