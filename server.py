#documentation for ThreadedSocketServer is from https://docs.python.org/3.5/library/socketserver.html
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    data = ""
    def handle(self):
        # self.request is the TCP socket connected to the client
        while 1:
            self.data = self.request.recv(1024).strip()
            if self.data == b'':
                break;
            print("{} wrote:".format(self.client_address[0]))
            print(self.data)
            # just send back the same data, but upper-cased
            self.request.sendall(self.data)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
    server_close()