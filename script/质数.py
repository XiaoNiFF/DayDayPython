""" 
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
             print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数') 
"""

""" 
def zhishu(aNum):
    # aNum = int(input('请输入计算多少以内的质数'))
    aLi = []
    for i in range(2,aNum+1):
        for j in range(2,i):
            if i % j == 0:break
        else:aLi.append(i)
    return aLi


if __name__ == '__main__':
    print(zhishu(100))

 """

def zhishu(aNum):
    # aNum = int(input('请输入计算多少以内的质数'))
    aLi = []
    for i in range(2,aNum+1):
        iszhishu = True
        for j in range(2,i):
            if i % j == 0:
                iszhishu = False
                break
        if iszhishu == True:aLi.append(i)
    return aLi

if __name__ == '__main__':
    print('100以内的质数为：',zhishu(100))