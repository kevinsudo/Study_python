from multiprocessing import Process
import os
def add_fun(a,b):
    print("子进程是%d,父进程是%d"%(os.getpid(),os.getppid()))
    return a+b
p=Process(target=add_fun,args=(2,3))
print("程序开始了")
p.start()
print(p.add_fun)
p.join()
print("进程结束")

