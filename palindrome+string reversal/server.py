import socket
import time

s = socket.socket()
s.bind(('localhost',9999))
s.listen(10)
print("Server listening on port 9999")

while True:
    c,c_addr = s.accept()
    print("connection established")
    
    start = time.time()     #timer
    
    #recv the string to reverse and palindrome check
    palindrome = False
    str = c.recv(1024).decode()
    print("string to check: ",str)
    
    str_rev = str[::-1]
    print("reversed string: ",str_rev)
    print("Server checking for palindrome...")
    
    if str == str_rev:
        print("It is a palindrome.\n")
        palindrome = True
    else:
        print("It is NOT a palindrome.\n")

    end = time.time()
    dur = end - start
    print("Duration for connectivity: ",dur)
    
    with open("file.txt","a") as file:
        file.write(f"String recv from client: {str} \n String after reversal : {str_rev} \n Is String Palindrome? {palindrome} \n\n")
    
    c.close()