""" 
# 猜大小
num = 100
while True:
    guess = int(input("请输入一个数值："))
    if guess == num:
        r = True
        print("正确")
        break
    elif guess < num:
        print("小了")
    else:
        print("大了")
        
# 保留字
import keyword
keyword.kwlist

# 列表
arr = ['False', 'None', 'True', 'and', 
    'as', 'assert', 'async', 'await', 
    'break', 'class', 'continue', 'def', 
    'del', 'elif', 'else', 'except', 
    'finally', 'for', 'from', 'global', 
    'if', 'import', 'in', 'is', 'lambda', 
    'nonlocal', 'not', 'or', 'pass', 'raise', 
    'return', 'try', 'while', 'with', 'yield']
arr[2:5]

print("hello\nworld")
print(r"hello\nworld")

input("\n\n按下 enter 键后退出。")

import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)


a = b = c = 1
print(a,c,b)
a, b, c = 1, 2, 'asucani'
print(a,b,c)

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

inputWords = ("i love asucani").split(" ")
print(inputWords[-1::-1])

import math
print(math.log(100,10))

import random as rd
print(rd.random())
rd.choice(("i love you",'hahah','hehehe'))
rd.randrange(1,100,1)
rd.uniform(1,100)

math.sin(math.radians(30))

math.e

print('\v')

"a" not in "abc"# 猜大小
num = 100
while True:
    guess = int(input("请输入一个数值："))
    if guess == num:
        r = True
        print("正确")
        break
    elif guess < num:
        print("小了")
    else:
        print("大了")
        
# 保留字
import keyword
keyword.kwlist

# 列表
arr = ['False', 'None', 'True', 'and', 
    'as', 'assert', 'async', 'await', 
    'break', 'class', 'continue', 'def', 
    'del', 'elif', 'else', 'except', 
    'finally', 'for', 'from', 'global', 
    'if', 'import', 'in', 'is', 'lambda', 
    'nonlocal', 'not', 'or', 'pass', 'raise', 
    'return', 'try', 'while', 'with', 'yield']
arr[2:5]

print("hello\nworld")
print(r"hello\nworld")

input("\n\n按下 enter 键后退出。")

import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)


a = b = c = 1
print(a,c,b)
a, b, c = 1, 2, 'asucani'
print(a,b,c)

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

inputWords = ("i love asucani").split(" ")
print(inputWords[-1::-1])

import math
print(math.log(100,10))

import random as rd
print(rd.random())
rd.choice(("i love you",'hahah','hehehe'))
rd.randrange(1,100,1)
rd.uniform(1,100)

math.sin(math.radians(30))

math.e

print('\v')

"a" not in "abc" 

x = 1
print(f'{x+1=}')

'hello'.center(20,'-')

'hello'.find('lo')

a = 'asucani'
print(f'{a:-<11}')

123%100
"""
""" 两个数比大小
def bidaxiao(a,b):
    if a > b:
        return a
    elif a == b:
        return '相等'
    else:
        return b

print(bidaxiao(6,3)) 
"""

""" 三个数比大小
def bdx(a,b,c):
    s = a
    for i in [a,b,c]:
        if i>s:s=i
    return s

print(bdx(10,2,5))
 """


""" 从大到小排序
sarr = {4,2,3,6}
larr = []
 
while len(sarr)>0:
    max=0
    for i in sarr:
        if i>max:max=i
    sarr.discard(max)
    larr.append(max)
    
print(larr)
 """

