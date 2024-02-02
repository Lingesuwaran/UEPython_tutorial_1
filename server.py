import sys
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',5001))

server.listen()

while True:
    client,address = server.accept()
    print('Connected')
    val = client.recv(1024).decode('utf-8')
    print(val)
    if val == 'close':
        client.close()
        sys.exit()
    elif val == 'Hi':
        client.send('Hello'.encode('utf-8'))
    else:
        client.send('Aloha'.encode('utf-8'))
    client.close()