import socket
import time

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num*factorial(num-1)
    

def isPrime(num):
    for i in range(2,num+1):
        if num%i == 0:
            return False    # If divisible, it's not prime

    return True

def fib(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)

s = socket.socket()
s.bind(("localhost",9999))
s.listen(10)
print("Server listening on port 9999")

while True:
    c,c_addr = s.accept()
    start = time.time()     #timer 
    print("connection established")
    
    num = c.recv(1024).decode()   #string 
    num = int(num)
    
    print("Checking if Factorial of number...")
    fact = factorial(num)
    print("Factorial: ", fact)
    
    print("Checking if number is prime...")
    prime = isPrime(num)
    print(f"Is number prime: {prime} ")
    
    print("Fibonacci Sequence...")
    fibo = fib(num)
    print(f"Fib Seq: {fibo} ")
    
    end = time.time()
    dur = end-start
    
    with open("file.txt","a") as file:
        file.write(f'Number from client: {num} \nFactorial of {num}: {fact} \nIs {num} Prime? {prime}\nFibonacci: {fibo} \nDuration Of connection: {dur}\n')
    
    c.close()
    
    
    
    
    