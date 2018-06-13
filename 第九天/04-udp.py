from socket import socket,AF_INET,SOCK_DGRAM
import struct
filename="test.txt"
udpsocket=socket(AF_INET,SOCK_DGRAM)
toaddr=("localhost",69)
massage=struct.pack("!H8sb5sb",1,filename.encode(),0,b"octet",0)
udpsocket.sendto(massage,toaddr)
recedata=udpsocket.recvfrom(1024)
print(recedata)
data=struct.unpack("!HH",recedata[0][:4])
print(data)
if data[0]==3:
    print("correct")
    f=open(filename,"w")
    f.write(recedata[0][4:])
    f.close()
udpsocket.close()
