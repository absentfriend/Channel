import requests
import string
import os
import re
from requestget import geturl
from requestget import posturl
from lxml import etree
url='http://news.wisesz.cc/mingcheng/api/v1//telecast/channels'
headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 5.1.1; EGREAT_A5_CN Build/LMY48W)'}
data={'':''}
r=posturl(url,data=data,headers=headers)
r=r.encode('utf-8').decode('unicode_escape')
title=re.findall(r'title":"(.+?)"',r)
m3u8=re.findall(r'play_url":"(.+?)"',r)
for m in m3u8:
    m3u8[m3u8.index(m)]=m.replace('\\','')
d=dict(zip(title,m3u8))
print(d)
