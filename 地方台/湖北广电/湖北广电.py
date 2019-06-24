import requests
import os
import re
from DPL频道列表模板 import lists
file=open("C:\\Users\\Administrator\\PycharmProjects\\频道破解\\湖北广电.txt","r+",encoding='utf-8')
f=file.read()
name=re.findall(r'no\n(.+?)\nhttp',f)
url=re.findall(r'http.+?no',f)
print(len(name))
print(len(url))
with open('湖北广电.dpl', 'w', encoding="utf-8") as f: f.write('')
with open('湖北广电.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0\n')
for u in url:
    j=url.index(u)
    (x,y)=lists(name[j], u)
    with open('湖北广电.dpl', 'a+', encoding="utf-8") as f: f.write(str(j + 1) + x + "\n" + str(j + 1) + y + "\n" + str(j + 1) + '*played*0\n')
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\湖北广电.dpl')