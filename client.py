#documentation for ThreadedSocketServer is from https://docs.python.org/3.5/library/socketserver.html
#Reference to http://effbot.org/tkinterbook/tkinter-index.htm for Tkinter

import socket
#import sys #will implement parsing args later
import tkinter as tk

HOST, PORT = "localhost", 9999

class chatGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Chat Room")
        self.make_widgets()
        
    def make_widgets(self):
        # Introduction label
        self.label = tk.Label(self, text="Hello, welcome to Milly's Chatroom (tentative)")
        self.label.pack(fill='x')
        
        # Holds listbox and scrollbar of message window
        self.message = tk.PanedWindow()
        self.message.pack(fill=tk.BOTH)
        
        scrollbar = tk.Scrollbar(self.message)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.messagebox = tk.Listbox(self.message, yscrollcommand=scrollbar.set)
        self.messagebox.pack(fill=tk.BOTH)
        
        scrollbar.config(command=self.messagebox.yview)
        
        # Textbox of data to send
        var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=var)
        self.entry.pack(fill=tk.X)
        
        # Sends data from the entry to the server
        self.bt = tk.Button(self, text="Submit", command=self.sendData)
        self.bt.pack()
        
    def sendData(self):
        # Create a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            #get data from entry
            data = self.entry.get()
            
            # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.sendall(bytes(data + "\n", "utf-8"))
            
            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")
            
            # Writes back response to the message box
            self.messagebox.insert(tk.END, received)
        
    def exitProgram():
        self.quit()

chat = chatGUI()
chat.mainloop()