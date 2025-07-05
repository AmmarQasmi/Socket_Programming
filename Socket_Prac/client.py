import socket
c = socket.socket()

c.connect(("localhost",9999))
print("Connected with the server on port 9999")

num1 = input("Enter first num: ")
num2 = input("enter 2nd number: ")
op = input("Enter operator")

data = f'{num1},{num2},{op}'        #2,2,+
c.send(data.encode())
print(f"{data} sent successfully")

print("Ans: ",c.recv(1024).decode())

