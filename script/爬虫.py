import requests
from bs4 import BeautifulSoup
import re

class pachong:

    def __init__(self, url):
        self.url = url

    def get_resp(self):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 Edg/81.0.416.68'}
        return requests.get(self.url, headers=headers)

    def get_text(self):
        # resp = pachong.get_resp(self)
        resp = self.get_resp() #功能和上面一样
        ls = []
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            for item in soup.find_all('span', 'short'):
                ls.append(item.string)
        return ls
    
    def get_allstar(self):
        ptn = re.compile(r'<span class="allstar(.*?) rating" title="\w*"></span>')
        ls = ptn.findall(self.get_resp().text)
        total = 0
        for i in ls:
            total += int(i)
        return total
        

if __name__ == "__main__":
    url = "https://movie.douban.com/subject/30488569/comments?status=P"
    douban = pachong(url)
    print(douban.get_text())
    print(douban.get_allstar())
