import socket
updsocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sendAddr=("192.168.1.7",9999)
updsocket.sendto(b"this is a test",sendAddr)
recvData=updsocket.recvfrom(1024)
print(recvData)
updsocket.close()
