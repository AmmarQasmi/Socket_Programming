import socket

s = socket.socket()

# Binding: port and address
s.bind(('localhost', 9999))

# Listen for limited client connections
s.listen(5)
print("Waiting for client connection")

# Accept client connection
while True:
    client_socket, client_addr = s.accept()
    print("Server accepted connection from client:", client_addr)
    
    # Communication: use client socket
    client_socket.send("Hello Client, Tell me your name.".encode())
    
    name = client_socket.recv(1024).decode()  # 1024 bytes can be received at max
    
    print(f"Got it {name}")
    
    # Close the connection (optional, or keep it open for further communication)
    client_socket.close()

s.close()
