from tkinter import *
from functools import partial

class Main():
    def Client(root):
        from clientelab4.clientProtocolHandler import main
        main(root)
    def Exit():
        exit()

    root = Tk()
    Canvas(root, width = 500, height = 200).pack()
    Button(root, text=("Connect"), command= partial(Client, root)).pack()
    Button(root, text=("Quit"), command = Exit).pack()
    mainloop()