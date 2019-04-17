from tkinter import *
from checkbox import *

base = Tk()
label = Label(base, text = "eat shit")
check_box = Check_box(base)
check_box.canvas.pack()
label.pack()
base.mainloop()
