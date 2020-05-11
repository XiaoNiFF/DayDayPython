# best_university_rate_2.py
# 面向对象式编程

import requests
from bs4 import BeautifulSoup
import bs4

class Pachong:
    '''定义一个爬虫类，传入URL参数'''
    def __init__(self, url):
        self.__url = url
    
    def getResp(self):
        '''Get请求返回（response对象）'''
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 Edg/81.0.416.68'}
        try:
            r = requests.get(self.__url, headers = headers)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r
        except:
            return 'HTTPError - 请求错误'
    

class Bestdaxue(Pachong):
    '''Pachong类的派生类'''
    def __getSoup(self):
        '''定义私有方法，返回soup对象'''
        r = self.getResp()
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
    paiming(100)