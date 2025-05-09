import threading
import socket


class Client:
    def __init__(self, host, port, nick):
        self.host = host
        self.port = port
        self.nick = nick

    def connect(self):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client = client
            self.client.connect((self.host, self.port))
        except ConnectionRefusedError:
            print(f"The server {self.host} is currently down and not taking any connections.")

    def recieve(self):
        while True:
            try:
                message = self.client.recv(1024).decode('ascii')
                if message == "REQ_NICK":
                    self.client.send(self.nick.encode('ascii'))
                else:
                    print(f"{message}")
            except:
                print("An ERROR occurred!")
                self.client.close()
                break

    def write(self):
        while True:
            message = f"{self.nick}: {input("")}"
            self.client.send(message.encode('ascii'))

    def start(self):
        recieve_thread = threading.Thread(target=self.recieve)
        recieve_thread.start()

        write_thread = threading.Thread(target=self.write)
        write_thread.start()


if __name__ == "__main__":
    host= input("Enter the server address: ")
    port = 47777

    nick = input("Enter your nickname: ")

    client = Client(host=host, port=port, nick=nick)
    client.connect()
    client.start()
