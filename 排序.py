# 排序
def paixu(arrSet):
    brrLi=[]
    while len(arrSet)>0:
        max=0
        for i in arrSet:
            if i>max:max=i
        arrSet.discard(max)
        brrLi.append(max)
    return brrLi        

arrSet = {3,1,2,4,7}
aLi = paixu(arrSet)
print(aLi)
print(aLi[::-1])