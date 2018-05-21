# Server

import socket
import sys
import random
import array
import re
import select 

def within(guess, random, med):
    dif = abs(random - guess)
    if dif == 0:
        return 0
    elif dif < med and dif > 0:
        return 1
    else:
        return 2


#client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind(("127.0.0.1", 4000))
client.listen(5)

#admin
admin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
admin.bind(("127.0.0.1", 4001))
admin.listen(5)

FIRST = 1
SECOND = 2
THIRD = 3

sockets = []
adresses = []
rnd = {}
steps ={}


sockets.append(client)
sockets.append(admin)

while True:
    ( r, w, e) = select.select(sockets, [], [])
    


    for variable in r:
        if (  variable == client):
            (conn,addr) = variable.accept()
            sockets.append(conn)
            adresses.append(addr)
            
            
            info = conn.recv(80).decode().strip()
            if ( info == "Hello"):
                conn.send("Greetings\r\n".encode())
                info = conn.recv(80).decode().strip()
                if ( info == "Game"):
                    conn.send("Ready\r\n".encode()) 
            
           
            randomNumber = random.randrange(0,30)
            rnd[conn] = randomNumber
            

                    
            
        elif  (variable == admin):
              
            (conn,addr) = variable.accept()            
            info = conn.recv(80).decode().strip()
            
            if ( info == "Hello"):
                conn.send("Admin-Greetings\r\n".encode())
                info = conn.recv(80).decode().strip()
                if ( info == "Who"):                    
                    adress = " "
                    for elements in adresses:
                        adress += str(elements[0]) + " " + str(elements[1]) + "\n"
                        conn.send(adress.encode())

        else :

            number = conn.recv(80).decode()
            number = int(number.split(":")[1])
            final = within(number, rnd[conn],3)
            if (final == 0):
                conn.send("Correct\r\n".encode())
                conn.close()
                break
            else:
                if ( final == 1) :
                    conn.send("Close\r\n".encode())
                    
                elif ( final == 2):
                    conn.send("Far\r\n".encode())

















        
        
