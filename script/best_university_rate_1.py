# best_university_rate_1.py
# 函数式过程编程

import requests
from bs4 import BeautifulSoup
import bs4

def getHtmlText(url):
    headers = {'User-Agent':'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 Edg/81.0.416.68'}
    try:        
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'HTTPError'

def parserHtml(html):
    ls = []
    soup = BeautifulSoup(html, 'lxml')
    for tr in soup.tbody.children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ls.append([tds[0].string, tds[1].string, tds[3].string])
    return ls

def printFormat(ls, num):
    str = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(str.format('排名', '大学', '总分', chr(12288)))
    for i in range(num):
        print(str.format(ls[i][0], ls[i][1], ls[i][2], chr(12288)))

def showResult(url, num):
    html = getHtmlText(url)
    ls = parserHtml(html)
    printFormat(ls, num)

if __name__ == "__main__":
    showResult('http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html', 100)