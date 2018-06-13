from socket import socket,AF_INET,SOCK_DGRAM
import struct
udpsocket=socket(AF_INET,SOCK_DGRAM)
toaddr=("localhost",69)

massage=struct.pack("!H8sb5sb",1,b"test.txt",0,b"octet",0)
udpsocket.sendto(massage,toaddr)
udpsocket.close()
