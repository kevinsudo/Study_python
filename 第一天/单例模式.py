class User(object):

    __instance=None
    def __init__(self,name):
        self.name=name
    @classmethod
    def get_instance(cls,name):
        if not cls.__instance:
            cls.__instance=User(name)
        return cls.__instance
#u1 =User("zs")
#u2 =User("ls")
u1 =User.get_instance("zs")
u2 =User.get_instance("ls")
print(u1==u2)#判断表达式如果返回True,这两个对象是一个对象，并且内存地址相同)
print("u1对象的内存地址是：%s,u2对象的内存地址是：%s"%(id(u1),id(u2)))
