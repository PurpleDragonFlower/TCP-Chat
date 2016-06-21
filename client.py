#documentation for ThreadedSocketServer is from https://docs.python.org/3.5/library/socketserver.html
#will implement Tkinter later
import socket
import sys
#from tkinter import *
import tkinter as tk

class chatGUI(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.title("Chat Room")
		self.make_widgets()
		
	def make_widgets(self):
		self.label = tk.Label(self, text="Hello, welcome to Milly's Chatroom (tentative)")
		self.label.pack(fill='x')
		var = tk.StringVar()
		self.entry = tk.Entry(self, textvariable=var)
		self.entry.pack(fill='x')
		self.bt = tk.Button(self, text="Submit", command=sendData)
		self.bt.pack()
		
	#put socket in here
	def sendData:
		pass
		
	def exitProgram():
		self.quit()

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

chat = chatGUI()
chat.mainloop()
	
print("Sent:     {}".format(data))
print("Received: {}".format(received))