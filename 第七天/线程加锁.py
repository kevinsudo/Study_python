import threading
import time

num=0
def work():
    print("线程开始")
    for i in range(20000):
        global num
        if suo.acquire():

            num+=1
            suo.release()
suo=threading.Lock()

for i in range(2):
    th=threading.Thread(target=work)
    th.start()
print(num)
