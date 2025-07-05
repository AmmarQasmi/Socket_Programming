import socket

s = socket.socket()  # Create socket (IPv4, TCP)
s.bind(("localhost", 9999))  # Bind to localhost on port 9999

s.listen(5)  # Listen for up to 5 clients
print("Server waiting for client to establish connection...")

while True:
    client_socket, client_addr = s.accept()
    print("Connection established with", client_addr)

    client_socket.send("What's your name?".encode())

    name = client_socket.recv(1024).decode()
    print("Client name:", name)

    # Receive numbers as a single string
    numbers = client_socket.recv(1024).decode()
    
    # Split and convert to integers
    num1, num2 = map(int, numbers.split(","))  #f"{num1},{num2}"
    print("Received numbers:", num1, num2)

    ans = str(num1 + num2)  # Convert result back to string before sending
    client_socket.send(ans.encode())

    client_socket.close()

s.close()
