class people:
    name = ''
    age = 0
    __weight = 0
    
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print(f'{self.name}说他{self.age}岁了!')

class student(people):
    def __init__(self,n,a,w,g):
        super(student,self).__init__(n,a,w)
        self.grade = g
    def speak(self):
        print(f'{self.name}说他{self.age}岁了，上{self.grade}年级!')


p = people('bailong', 99, 30)
p.speak()

s = student('bailong',99,30,8)
s.speak()
