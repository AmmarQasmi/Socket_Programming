import socket

c = socket.socket()

c.connect(("localhost",9999))

query1 = c.recv(1024).decode() #shape
shape = input("Enter shape: ")
c.send(shape.encode())

query2 = c.recv(1024).decode() #area or parameter
op = input("Area or Parameter: ")
c.send(op.encode())

data = c.recv(1024).decode()

if shape == 'square':
    l = input(f"enter side size of {shape}: ")
    c.send(l.encode())
else: 
    l = input(f"enter length of {shape}: ")
    b = input(f"enter breadth of {shape}: ")
    ans = f"{l},{b}"
    c.send(ans.encode())
    
final = c.recv(1024).decode()
print("Ans: ",final)


