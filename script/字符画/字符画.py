from PIL import Image
arrLi = ['@','#','$','%','&','?','*','o','/',
    '{','[','(','|','!','^','~','-','_',':',',',';','.','`','"']
count = len(arrLi)

def toText(image_ojb):
    aStr = ''
    for h in range(image_ojb.size[1]):
        for w in range(image_ojb.size[0]):
            r,g,b=image_ojb.getpixel((w,h))
            grayNum = int(r*0.229+g*0.587+b*0.114)
            aStr += arrLi[int(grayNum*(count/255)-1)]
        aStr += '\n'
    return aStr

im = Image.open('pkq.jpg')
txt = open('pkq.txt', 'a')
txt.write(toText(im))
txt.close()