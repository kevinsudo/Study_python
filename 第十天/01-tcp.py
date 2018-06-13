from socket import socket,AF_INET,SOCK_STREAM
seversocket=socket(AF_INET,SOCK_STREAM)
severaddr=("192.168.1.7",8399)
seversocket.bind(severaddr)

seversocket.listen(5)
clientsocket,clientaddr=seversocket.accept()

recedata=clientsocket.recv(1024)
clientsocket.send(b"hello")
seversocket.close()
clientsocket.close()
