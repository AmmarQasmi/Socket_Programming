import socket

s = socket.socket()
s.bind(("localhost" , 9999))
s.listen(5)
print("listening on port 9999")
while True:
    c,c_addr = s.accept()
    
    c.send("Enter two numbers and operator to perform calculation in format (num1,num2,op)".encode())
    print("Waiting for client to respond\n")
    
    data = c.recv(1024).decode()
    
    #split data in num1, num2, and operator current format (num1,num2,op)
    num1,  num2 , op = data.split(",")
    
    #typecast num1 and num2
    
    num1 , num2 = float(num1),float(num2)
    ans = 0
    print("received numbers: ",num1,num2)
        
    if op == '+':  
        ans = num1 + num2
        
    elif op == '-': 
        ans = num1 - num2
        
    elif op == '*': 
        ans = num1 * num2
   
    elif op == '/': 
        ans = num1 / num2
    else:
        result = "Invalid operator"
        
    #text file:
    with open("ans.txt","a") as file:
        file.write(f"{num1} {op} {num2} = {ans}")
        
    # # Send file to client
    # with open("result.txt", "rb") as file:
    #     file_data = file.read()
    #     c.sendall(file_data)  # Send entire file contents
        
    c.send(str(ans).encode())   
    
    
    c.close()
   
   #to send and receive files, we will open them in binary mode (rb,wb)