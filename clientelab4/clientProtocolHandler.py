from socket import *
from symbol import if_stmt
from threading import *

from tkinter import *

BUFFER_SIZE = 1024

class App:
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 27000
    client = socket(AF_INET, SOCK_STREAM)
    paso = 1
    server = (HOST, PORT)
    client.connect(server)

    def __init__(self, master):
        frame = Frame(master)
        frame.grid(row=2, column=3)

        self.quitbutton = Button(frame, text="QUIT", fg='red',
                                 command=frame.quit)
        self.quitbutton.grid(row=1, column=2)

        self.button = Button(frame, text="SEND", command=self.Send)
        self.button.grid(row=1, column=1)

        self.sendtext = Entry(frame, width=60)
        self.sendtext.grid(row=1, column=0)

        gettext = Text(frame, height=10, width=80, wrap=WORD)
        self.gettext = gettext
        gettext.grid(row=0, columnspan=3)
        gettext.insert(END, 'Connection ongoing with server\n')
        # Receive the folders available
        folders = self.client.recv(1024).decode("utf-8")
        # First send to the server which folder to ask for
        gettext.insert(END, "Options: " + folders + "\n")
        gettext.insert(END, "Folder to ask for:\n")
        gettext.configure(state='disabled')



    def Send(self):
        if self.paso == 1:
            self.gettext.configure(state='normal')
            text = self.sendtext.get()
            self.gettext.insert(END, '%s\n' % text)
            self.sendtext.delete(0, END)
            self.client.sendall(bytes(text, 'ascii'))
            self.gettext.configure(state='disabled')
            response = self.client.recv(BUFFER_SIZE).decode("utf-8")
            self.gettext.configure(state='normal')
            self.gettext.insert(END, '%s\n' % response)
            self.paso = 2
            self.gettext.insert(END, 'File to ask for? (From the list): \n')

        elif self.paso == 2:
            text = self.sendtext.get()
            self.gettext.configure(state='disabled')
            self.client.sendall(bytes(text, 'ascii'))
            with open("repo/" + text, 'wb') as f:
                pck = self.client.recv(BUFFER_SIZE)
                while pck:
                    f.write(pck)
                    pck = self.client.recv(BUFFER_SIZE)


# spawn the GUI
root = Tk()
root.title('Client')
app = App(root)
root.mainloop()