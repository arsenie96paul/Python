# Client

import socket
import sys

host = "127.0.0.1"
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))   


s.send("Hello\r\n".encode())

recieved = s.recv(80).decode().strip()
            
if recieved == "Greetings":
    s.send("Game\r\n".encode())
    
    recieved = s.recv(80).decode().strip()
    if recieved == "Ready":
        print("Welcome to the guess the number game!")

while True:

    try:
        
        InsertNumber = input("What is your guess? ")        
        
        s.send(("My guess is:" + InsertNumber).encode())
        recieved3 = s.recv(80).decode().strip()
        
        if recieved3 == "Far":
            print("You are way off.")
        elif recieved3 == "Close":
            print("You are close!")
        elif recieved3 == "Correct":
            print("You guessed correctly!")
            s.close()
            break            
            
    except ConnectionResetError:
        pass
        
    
