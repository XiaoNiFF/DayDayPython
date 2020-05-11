import requests
from bs4 import BeautifulSoup
import bs4
import os

class Pachong:
    '''定义一个爬虫类，传入URL参数'''
    def __init__(self, url):
        self.url = url
    
    def get_resp(self):
        '''Get请求返回（response对象）'''
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 Edg/81.0.416.68'}
        try:
            r = requests.get(self.url, headers = headers)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r
        except:
            return 'HTTPError - 请求错误'

def check_ip(ip):
    '''ip138查询ip信息'''
    url = "https://www.ip138.com/iplookup.asp?ip={}&action=2"
    txt = Pachong(url.format(ip)).get_resp().text
    print(txt[:1000])

def down_pic(root):
    '''下载url地址的文件到本地'''
    url = "http://image.ngchina.com.cn/2020/0508/20200508022628171.jpg"
    # root = os.getcwd()
    # root = "D://pics//"
    path = os.path.join(root, url.split('/')[-1])
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = Pachong(url).get_resp()
        with open(path, 'wb') as f:
            f.write(r.content)
            print('文件保存成功')
    else:
        print('文件已经存在')

def soup(url):
    '''输出url地址所有标签'''
    r = Pachong(url).get_resp()
    soup = BeautifulSoup(r.text, 'html.parser')
    for tag in soup.find_all(True):
        print(tag.name)
    

class Bestdaxue(Pachong):
    '''Pachong类的派生类'''

    def __getSoup(self):
        '''定义私有方法，返回soup对象'''
        r = self.get_resp()
        soup = BeautifulSoup(r.text, 'lxml')
        return soup
    
    def parserHtml(self):
        '''解析soup，返回包含所有大学的排名,名称,总分'''
        ls = []
        soup = self.__getSoup()
        for tr in soup.tbody.children:
            if isinstance(tr, bs4.element.Tag):
                tds = tr('td')
                ls.append([tds[0].string, tds[1].string, tds[3].string])
        return ls

    @staticmethod
    def printFormat(ls, num):
        '''静态方法，格式化输出'''
        str = "{0:^10}\t{1:{3}^10}\t{2:^10}"
        print(str.format('排名', '大学', '总分', chr(12288)))
        for i in range(num):
            print(str.format(ls[i][0], ls[i][1], ls[i][2], chr(12288)))

    def showResult(self, num):
        '''相当于main()函数'''
        ls = self.parserHtml()
        self.printFormat(ls, num)
        self.printFormat

def paiming(num):
    dxpm = Bestdaxue('http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html')
    dxpm.showResult(num)


if __name__ == "__main__":
    # check_ip('220.181.38.148')
    # down_pic(os.getcwd())
    # soup('https://python123.io/ws/demo.html')
    paiming(100)
    


