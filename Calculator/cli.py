import socket

c = socket.socket()

c.connect(("localhost",9999))
print("client connected successfuly")

query = c.recv(1024).decode()

name = input("Enter your name: ")

c.send(name.encode())
print("name sent successfully")