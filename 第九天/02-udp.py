from socket import socket,AF_INET,SOCK_DGRAM
import struct
udpsocket=socket(AF_INET,SOCK_DGRAM)
toaddr=("localhost",69)

massage=struct.pack("!H9sb5sb",1,b"test1.txt",0,b"octet",0)
udpsocket.sendto(massage,toaddr)
recedata=udpsocket.recvfrom(1024)
print(recedata)
udpsocket.close()
