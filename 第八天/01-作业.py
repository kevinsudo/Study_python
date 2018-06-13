from socket import socket,AF_INET,SOCK_DGRAM

udpsocket=socket(AF_INET,SOCK_DGRAM)
def sendmessage():
    print("我是kevin")
    sendAddr=("172.0.0.1",8899)
    udpsocket.sendto(b"this hello",sendAddr)
def recmessage():
    print("收到请回答，回复等待.....")
    bindaddr=("",8999)
    udpsocket.bind(bindaddr)
    udpsocket.recvfrom(1024)
if __name__=="__main__":
    recmessage()
    udpsocket.close()
