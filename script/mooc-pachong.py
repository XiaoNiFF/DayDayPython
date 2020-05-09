import requests
from bs4 import BeautifulSoup
import os

class Pachong:
    '''定义一个爬虫类，传入URL参数'''
    def __init__(self, url):
        self.url = url
    
    def get_resp(self):
        '''Get请求返回（request对象）'''
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 Edg/81.0.416.68'}
        try:
            r = requests.get(self.url, headers = headers)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r
        except:
            return 'HTTPError - 请求错误'

def check_ip(ip):
    url = "https://www.ip138.com/iplookup.asp?ip={}&action=2"
    txt = Pachong(url.format(ip)).get_resp().text
    print(txt[:1000])

def down_pic(root):
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



if __name__ == "__main__":
    # check_ip('220.181.38.148')
    down_pic(os.getcwd())


