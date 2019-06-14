import requests
from requestget import posturl
from requestget import geturl
import json
url='http://newlive.ahtv.cn/index/getSign'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36','Referer':'http://nettv.ahtv.cn/live/index.html?spm=zm5057-001.0.0.1.fgxDCv&jumpchannel=ahws'}
datas={'catalog':'/pull.bdflv.ahtv.cn/live/ahws2'}
r=posturl(url,data=datas,headers=headers)
print(r)
sign=r[9:41]
timestamp=r[-11:-1]
print(sign)
print(timestamp)
playurl='http://pull.bdflv.ahtv.cn/live/ahws2.flv?timestamp='+timestamp+'&secret='+sign
print(playurl)