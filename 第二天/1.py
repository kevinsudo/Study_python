class Person(object):
    def __init__(self,name):
        self.name=name
    def work(self,axe_type):
        print(self.name+"开始工作了")

#需要一把石斧

        Aex(axe_type).cut_tree()

class Aex(object):
    def __init__(self,name):
        self.name=name
    def cut_tree(self):
        if self.name=="stone":
            print("石斧头开始砍树")
        elif self.name=="steel":
            print("铁斧头开始砍树")
        else:
            print("输入斧头错误")
person =Person("zs")
person.work("stel")
