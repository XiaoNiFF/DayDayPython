import os

def find_py(path):
    aLi = []
    fileList = os.listdir(path)
    for fileName in fileList:
        fullPath = os.path.join(path,fileName)
        if os.path.isdir(fullPath):
            find_py(fullPath)
        elif fileName[-3:] == '.py':
            aLi.append(fullPath)
    return aLi

if __name__ == '__main__':
    print(find_py(os.getcwd()))