f=open("keivn.txt","r")
num=0
a=[]
a1=[]
num1=[]
while True:
    contend=f.readline()
    if contend=="":
        break
    elif contend=="\n":
        print("换行符%d"%num)
        num1.append(num)
    num+=1
    a.append(contend[0])
for i in num1:
    a[i]=None
for i in a:
    if i!=None:
        a1.append(i)
print(a1)

