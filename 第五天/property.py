class Test(object):
    def __init__(self,num):
        self.num=num
    @property
    def num(self):
            return self.__num
    @num.setter
    def num(self,num):
        if num>200:
            self.__num=num
test=Test(100)
#test.getnum()
test.num=400
print(test.num)

