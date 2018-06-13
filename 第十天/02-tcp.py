from socket import socket,AF_INET,SOCK_STREAM
clientsocket=socket(AF_INET,SOCK_STREAM)
severaddr=("192.168.1.7",10000)
clientsocket.connect(severaddr)

clientsocket.send(b"hello")

clientsocket.close()
