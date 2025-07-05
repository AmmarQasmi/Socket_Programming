import socket

c = socket.socket()

c.connect(("localhost",9999))
print("Client Connected with server")

str = input("Enter the string: ")
print(f'String: {str}')

c.send(str.encode())
print("String sent to server")

c.close()
