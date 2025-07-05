import socket
import time  

s = socket.socket()

s.bind(("localhost",9999))
s.listen(5)
print("server listening...")

area = 0 
para = 0

while True:
    start = time.time()     #time started
    c,c_addr = s.accept()
    print("connected with client...")
    
    c.send("square or rectangle?".encode())
    shape = c.recv(1024).decode()
    
    c.send("Area or parameter?".encode())
    operation = c.recv(1024).decode()
    
    if shape == 'square' and operation == 'area':
        c.send("Enter square side size: ".encode())
        side = c.recv(1024).decode()
        side = int(side)
        area = side*side
        c.send(str(area).encode())
        
    elif shape == 'square' and operation == 'parameter':
        c.send("Enter square side size: ".encode())
        side = c.recv(1024).decode()
        side = int(side)
        para = 4*side
        c.send(str(para).encode())
        
    elif shape == 'rectangle' and operation == 'area':
        c.send("Enter length and breadth of rectangle in format (l,b) ".encode())
        data = c.recv(1024).decode()
        l,b = data.split(",")
        l = float(l)
        b = float(b)
        area = l*b
        c.send(str(area).encode())
        
    elif shape == 'rectangle' and operation == 'parameter':
        c.send("Enter length and breadth of rectangle: ".encode())
        data = c.recv(1024).decode()
        l,b = data.split(",")
        l = float(l)
        b = float(b)
        para = 2*(l+b)
        c.send(str(para).encode())
    
    end = time.time()
    duration = end - start
    
    with open("file.txt","a") as file:
        file.write(f"Duration of connectivity: {duration} \n")
        file.write(f"{shape} & {operation}: ")
        if operation == 'parameter':
            file.write(f"{para} ")
        else:
            file.write(f"{area}")

    print("ans sent successfully")
    c.close()
    