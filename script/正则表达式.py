import re

s1 = "2020-4-20, hello world of python!"
s2 = "www.hao123.com"
s3 = "18868355283-18368687295"
s4 = "5RFT123VB - 5WCC163VB - 5RBM456VB - 5RCS123VB - 5RTF1234VB"
s5 = "abc我是中国人"

ptn = re.compile(r'[\u2E80-\u9FFF]+')
strNew = ptn.findall(s5)
print(strNew)

# ptn = re.compile(r'.*')
# ptn = re.compile(r'w{3}\.(.+)\..{2,3}')
# ptn = re.compile(r'(\d{11}).*(\d{11})')
# strNew = ptn.sub(r'\1\n\2',s3)
# print(strNew)
# mat = ptn.match(s1)
# print(mat.group())
# print(mat.group(1))
# # print(mat.group(2))
# print(mat.groups())

# ptn = re.compile(r'\d[A-Z]{3}(?=\d{3}VB)')
# mat = ptn.findall(s4)
# print(mat)

# ptn = re.compile(r'\d[A-Z]{3}(?!\d{3}VB)')
# mat = ptn.findall(s4)
# print(mat)

# ptn = re.compile(r'(?<!5RFT)\d{4}[A-Z]{2}')
# mat = ptn.findall(s4)
# print(mat)