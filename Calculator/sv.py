# server : bind, listen , accept 
# client: connect()
# socket

import socket

s = socket.socket() #ipv4/ipv6 , tcp/udp

s.bind(("localhost",9999))  #add and port merging

s.listen(5) #5 clients ka wait karega max
print("Server connected on port 9999 and waiting for client...")

while True:
    c_socket, c_addr = s.accept()
    print("server connected with the client ",c_addr )
    
    c_socket.send("Hey what is your name".encode())
    
    name = c_socket.recv(1024).decode()
    print("Client: " , name)
    
    c_socket.close()
    
#encode: string -> biary
# decode: binary -> string