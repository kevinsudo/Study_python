import os

pid=os.fork()
if pid<0:
    print("调用进程失败")
elif pid ==0:
    print("我是子进程，进程pid是%d,父进程是%d"%(os.getpid(),os.getppid()))
else:
    print("我是父进程，进程pid是%d，子进程是%d"%(os.getpid(),pid))
