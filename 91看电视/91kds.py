import time
from requestget import geturl
import random
import requests
import re
import os
import string
headers={'Referer':'http://m.91kds.org/jiemu_sdqdtv1.html','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
def get_livekey():
    auth = 'http://m.91kds.org/auth3.php?t=' + str(random.random())
    r = geturl(auth,headers=headers)
    livekey=re.findall(r'(nwtime.+?)"',r)
    livekey=livekey[0]
    return livekey
#print(get_livekey())
file=open("C:\\Users\\Administrator\\PycharmProjects\\频道破解\\91看电视\\91ktv.txt","r+",encoding='utf-8')
#得到livekey
f=file.read()
auth='http://m.91kds.org/auth3.php?t='+str(random.random())
r=geturl(auth,headers=headers)
#print(r)
n1=r.find('":"')+len('":"')
n2=r.find('"',n1)
livekey=r[n1:n2]

def qtv(a,b):
    qtv_url='http://v.91kds.cn/b9/'+a+'.m3u8?id='+b+'&'+livekey
    #print(qtv_url)
    headers2 = {'Referer': 'http://m.91kds.org/jiemu_cctv1.html',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
                'Accept-Encoding': 'identity;q=1, *;q=0', 'chrome-proxy': 'frfr', }
    r=geturl(qtv_url,headers=headers2)
    return r

qyname=re.findall(r'"name": "(爱奇艺.+?)"',f)
qyid=re.findall(r'ename": "(qiyi.+?)"',f)
qyd=dict(zip(qyname,qyid))
'''
with open('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\爱奇艺\\iqiyi.txt', 'w', encoding="utf-8") as f: f.write('')
for y,x in qyd.items():
    qy1=qiyi2('qiyi2',x)
    n=qy1.find('m3u8')+4
    qy1=qy1[0:n]
    qy1=qy1.replace('hlslive.video.ptqy.gitv.tv','113.113.73.41/r/baiducdnct.inter.iqiyi.com')
    #qiyiurl.append(qy1)
    print(y,qy1)
    with open('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\爱奇艺\\iqiyi.txt', 'a+', encoding="utf-8") as f: f.write(y+','+qy1+'\n')
#print(len(qiyiurl))
'''

def get_location(n,b):
    url='http://v.91kds.cn/b9/'+n+'.m3u8?id='+b+'&'+livekey
    #print(url)
    r=requests.get(url,headers=headers,allow_redirects=False)
    #print(r.headers)
    if str(r.headers).find("http")==-1:
        la=''
    else:
        la=r.headers['location']
    return la
def area(s):
    print(s+'*************************************************')
    s1=re.findall(s+'\.m3u8\?id=(.+?)&',f)
    print(s1)
    for x in s1:
        a = get_location(s, x)
        print(x, a)
def area2(s):
    print(s+'*************************************************')
    s1=re.findall(s+'\.m3u8\?id=(.+?)&',f)
    print(s1)
    for x in s1:
        a = qtv(s, x)
        #print(x, a)
#bstsh=area2('bstsh')
qtv=area2('sdqdtv')
pptv=area2('pptv')
cutv=area('cutv1')
hatv=area('hatv')
hntv=area('hntv')
ahtv=area('ahtv')
hljtv=area('hljtv')
qiyi2=area('qiyi2')
cibn=area('rmsx')
gdsztv=area('gdsztv')
gdgztv=area('gdgztv')
#sdqk1=area('sdqk1')
hncscs=area('hncscs')
file.close()