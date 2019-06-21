import requests
from requestget import posturl
from requestget import geturl
import re
u1='https://www.yyrtv.com/'
h1={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36','Cookie':'zycna=cpVarJqd/MsBAT2QkG22Vt/m; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; Hm_lvt_52ca1c67e4ae3d21a3cb493fcc180fe3=1560995517,1560999416; Hm_lpvt_52ca1c67e4ae3d21a3cb493fcc180fe3=1560999416'}
r1=geturl(u1,headers=h1)
rtmp=re.findall(r'rtmp://.+?liveevent',r1)
name=re.findall(r'<p title="(.+?)"',r1)
name=name[16:19]
d=dict(zip(name,rtmp))
for a,b in d.items():
    print(a,b)