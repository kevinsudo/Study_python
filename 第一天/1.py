class Person(object):
    def __init__(self,name):
        self.name=name
    def work(self,axe_type):
        print(self.name+"开始工作了")

#需要一把石斧
        aex=Factory.creat_aex(axe_type)
        aex.cut_tree()

class Aex(object):
    def __init__(self,name):
        self.name=name
    def cut_tree(self):
        print("%s斧头开始砍树"%self.name)
class StoneAex(Aex):
    def cut_tree(self):
        print("使用石头做的斧头砍树")
class SteelAex(Aex):
    def cut_tree(self):
        print("使用钢铁做的斧头砍树")
class Factory(object):

    def creat_aex(type):
        if type=="stone":
            return StoneAex("花岗岩斧头")
        elif type=="steel":
            return SteelAex("钢铁斧头")
        else:
            print("传入类型不对")

p = Person("原始人zs")
p.work("steel")
