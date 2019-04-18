from tkinter import *
from checkbox import *
from tagporter import *

base = Tk()
label = Label(base, text = "eat shit")

tag_porter = Tag_porter(base)
tag_porter.canvas.pack()

check_box = Check_box(base)
check_box.canvas.pack()

label.pack()
base.mainloop()
