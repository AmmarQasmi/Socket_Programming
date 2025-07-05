#bind , listen, accept -> server
#connect -> client
# common -> socket creation

import socket
import time

s = socket.socket()

s.bind(("localhost",9999))      #merges address and port#
s.listen(5) #5 clients ko cater krsakta hai at max
print("Server listening n port 9999")

while True:
    c_socket, c_addr = s.accept()
    print("Connection established")
    start = time.time()
    
    data = c_socket.recv(1024).decode() #2,2,+
    num1,num2,op = data.split(",")
    ans = 0
    
    num1 = float(num1) 
    num2 = float(num2)
    
    if op == '+':
        ans = num1 + num2
    if op == '-':
        ans = num1 - num2
    if op == '*':
        ans = num1 * num2
    if op == '/':
        ans = num1 / num2
    
    c_socket.send(str(ans).encode())
    print(f"answer: {ans} sent. ")
    
    end = time.time()
    dur = end - start
    print("duration of connectivity: ", dur)
    
    
    #filing
    
    with open("file.txt","a") as file:
        file.write(f"Duration : {dur} \nClient Query: {num1} {op} {num2} = {ans}\n")
    
    
    c_socket.close()
