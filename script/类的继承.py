class DemoClass:
       count = 0
       def __init__(self, name):
              self.__name = name
              DemoClass.count += 1
       def getName(self):
              return self.__name

class Humandc(DemoClass):
       count = 10
       def printName(self):
              return str(DemoClass.count) + self.getName() + '同志'

hdc1 = Humandc('张三')
hdc2 = Humandc('李四')
hdc3 = Humandc('王五')
print(hdc1.getName())
print(hdc1.printName())
# print(DemoClass.count)