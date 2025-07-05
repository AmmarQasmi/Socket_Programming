import socket

c = socket.socket()

# client doesn't bind or listen it is servers job, instead it connects with the server

c.connect(('localhost',9999))
print("Connected with server successfully")

#communication:
server_message = c.recv(1024).decode()  #server asked for name
print("Server: ",server_message)

# Send name to server
name = input("Enter your name: ")
c.send(name.encode())

c.close() 