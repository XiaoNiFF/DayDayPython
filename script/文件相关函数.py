import os

ls = []
def getpyfile(path):
    # path = "C:\Users\bailong\Documents\python\hello"
    filelist = os.listdir(path)
    try:
        for each in filelist:
            fullpath = os.path.join(path,each)
            if os.path.isdir(fullpath):getpyfile(fullpath)
            elif fullpath[-3:].lower() == ".py":ls.append(each)
    except:
        pass
    return ls

if __name__ == "__main__":
    ls = getpyfile(r"C:\Users\bailong\Documents\python\hello\111")
    print(ls)



