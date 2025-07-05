import socket

c = socket.socket()
c.connect(("localhost", 9999))

print("Connection established")

# Receive message from the server
server_message = c.recv(1024).decode()
print(server_message)

# Send name
name = input("What's your name: ")
c.send(name.encode())

# Send numbers in a single message
num1 = 2
num2 = 3
numbers = f"{num1},{num2}"  # Use a comma as a separator
c.send(numbers.encode())

print("NUM1 and NUM2 sent:", num1, num2)

# Receive and print the result
ans = c.recv(1024).decode()
print("Sum of num1 and num2 =", ans)

c.close()
