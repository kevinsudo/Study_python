from multiprocessing import Pool
import time
import os
def work(a):
    time.sleep(2)
    print("子进程%d，id%d"%(a,os.getpid()))

pool=Pool(3)
for x in range(10):
    pool.apply_async(work,(x,))
pool.close()
pool.join()
print("结束")
