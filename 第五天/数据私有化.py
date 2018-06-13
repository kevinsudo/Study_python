class Test(object):
    def __init__(self,num):
        self.num=num
    def getnum(self):
            print( self.__num)
    def setnum(self,num):
        if num>200:
            self.__num=num
test=Test(100)
#test.getnum()
print(test.num)
