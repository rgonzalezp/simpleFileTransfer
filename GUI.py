from tkinter import *

class Main():
    def Client():
        from clientelab4.clientProtocolHandler import main
        main()
    def Server():
        from servidorlab4.serverFiles import main
        main()
    def Exit():
        exit()

    root = Tk()
    Canvas(root, width = 300, height = 100).pack()
    Button(root, text=("Client"), command = Client).pack()
    Button(root, text=("Server"), command = Server).pack()
    Button(root, text=("Quit"), command = Exit).pack()
    mainloop()