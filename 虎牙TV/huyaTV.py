import requests
import string
import os
import re
from requestget import geturl
from DPL频道列表模板 import lists
headers={"referer": "https://www.huya.com/l","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}
yiqikan="http://www.huya.com/g/2135"
rx=geturl(yiqikan,headers)
#print(rx)
p1=r"https://www.huya.com/[1-9]{7,9}"
pattern1=re.compile(p1)
roomid=re.findall(r'(https://www.huya.com/.+?)" class="title new-clickstat" report=',rx)
title=re.findall(r'target="_blank">(.+?)</a>',rx)
urls=[]
for x in roomid:
    i=roomid.index(x)
    url=x
    r=geturl(url,headers=headers)
    n1=r.find('"sHlsUrl":"')
    n2=r.find('","',n1)
    r1=r[n1+len('"sHlsUrl":"'):n2]
    r2=r1.replace('\\','')
    n3=r.find('"sStreamName":"')+len('"sStreamName":"')
    n4=r.find('","sFlvUrl":"')
    r3=r[n3:n4]
    playurl=r2+'/'+r3+'.m3u8'
    urls.append(playurl)
    print(title[i],playurl)
with open('虎牙一起看.dpl', 'w', encoding="utf-8") as f: f.write('')
with open('虎牙一起看.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0\n')
for u in urls:
    j=urls.index(u)
    (x,y)=lists(title[j],u)
    with open('虎牙一起看.dpl', 'a+', encoding="utf-8") as f: f.write(str(j+1)+x + "\n"+str(j+1)+y+"\n"+str(j+1)+'*played*0\n')
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\虎牙TV\\虎牙一起看.dpl')