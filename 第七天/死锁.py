import threading
import time
class Mysuo(threading.Thread):
    def work(self):
        if suo1.acquire():
            print("suo1开始加锁")
            time.sleep(2)
            if suo2.acquire():
                print("suo2开始加锁")
                suo2.release()
            suo1.release()
class Mysuo1(threading.Thread):
    def run(self):
        if suo2.acquire():
            print("suo2开始加锁")
            time.sleep(2)
            if suo1.acquire():
                print("suo1开始加锁")
                suo1.release()
            suo2.release()
if __name__=="__main__":
    suo1=threading.Lock()
    suo2=threading.Lock()
    mysuo=Mysuo()
    mysuo.start()
    mysuo1=Mysuo1()
    mysuo1.start()
