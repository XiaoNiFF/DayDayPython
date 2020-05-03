class DemoClass:
    '类对象DemoClass'
    count = 10 
    def __init__(self,n,a):
        self.name = n
        self.age = a
        DemoClass.count += 1
    
    @classmethod
    def clsmet(cls):
        DemoClass.count *= 10


cls1 = DemoClass('张三',30)
print(DemoClass.count)

cls2 = DemoClass('李四',35) 
print(DemoClass.count)

cls1.clsmet()
print(DemoClass.count)

cls2.clsmet()
print(DemoClass.count)

DemoClass.clsmet()
print(DemoClass.count)
