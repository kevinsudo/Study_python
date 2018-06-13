from multiprocessing import Process
import os
import time

#定义自己的进程类
class Myprocess(Process):
    def __init__(self,interval):
        super().__init__()
        self.interval=interval
    def run(self):
        print("子进程")
        start_time=time.time()
        time.sleep(self.interval)
        stop_time=time.time()
print("主进程")
stat_time=time.time()
p=Myprocess(4)
p.start()
p.join()
stop_time=time.time()
print("程序运行多少秒%d"%(stop_time-stat_time))
