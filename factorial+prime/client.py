import socket

c = socket.socket()

c.connect(('localhost',9999))
print("connection established")

num = input("Enter number for finding Factorial, Prime Check , & Fibonacci Sequence: ")

c.send(num.encode())
print(f"{num} sent to Server. Go to server's terminal to find out ans or find them in file.txt. ")

c.close();