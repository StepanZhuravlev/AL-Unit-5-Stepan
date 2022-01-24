from tkinter import *
def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text = selection)

root = Tk()
var = IntVar()
Radiobutton(root, text="Option 1", variable=var, value=1, command=sel).pack(anchor=W)
Radiobutton(root, text="Option 2", variable=var, value=2, command=sel).pack(anchor=W)
Radiobutton(root, text="Option 3", variable=var, value=3, command=sel).pack(anchor=W)
label = Label(root)
label.pack()
root.mainloop()