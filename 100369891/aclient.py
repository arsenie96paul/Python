#Admin
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 4001))


s.send('Hello\r\n'.encode())
info = s.recv(80).decode()
if ( info == "Admin-Greetings\r\n" ):
    
    s.send("Who\r\n".encode())
    print ( "The players currently playing are:")
    info = s.recv(10000).decode()
    print(info)
s.close()
