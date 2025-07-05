import socket

c = socket.socket()

c.connect(("localhost",9999))
print("Client connected to port 9999")

s = c.recv(1024).decode()
print(s);

num1 = input("Enter num1: ")
num2 = input("Enter num2: ")
op = input("Enter operator (+, -, *, /): ")

data = f"{num1},{num2},{op}" #2,2,+
print(data)
c.send(data.encode())

ans = c.recv(1024).decode()
print("Ans: ", ans)

# # Receive file from server
# file_data = c.recv(1024)

# # Save received file
# with open("received_result.txt", "wb") as file:
#     file.write(file_data)

# print("Result file received and saved as 'received_result.txt'.")


c.close()