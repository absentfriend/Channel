#官网     http://www.yzntv.com/tvlist
#邗江，
import requests
import string
import os
import re
from requestget import geturl
from lxml import etree
url='http://www.yzntv.com/tvlist'
headers={'Cookie':'JSESSIONID=952C2BB01B51AC16F9B85630311623F7; UM_distinctid=16b6ddeef9031a-0fd2087250ae87-6353160-1fa400-16b6ddeef91978; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; u_t_0dfbd5c4476a8ffe3f02aca767156e5c=852682a2-c88d-4c34-a81a-23c46d7dcdaf; CNZZDATA1261166255=576782448-1560913678-null%7C1560911895','Referer':'http://www.yzntv.com/','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
r=geturl(url,headers)
#print(r)
html=etree.HTML(r)
#ch=html.xpath('//div[@class="live_list_div"]/@href')
ch=re.findall(r'(http://www.yzntv.com:80/maintab/livel\?cid=.+?)"',r)
cid=re.findall(r'maintab/livel\?cid=(.+?)&',r)
cid=cid[0:5]
ch=ch[0:5]
for i in cid:
    url='http://cc.linkinme.com/yztv/'+i
    print(url)
#print(ch)
tv=re.findall(r'tvname" title="(.+?)"',r)
tv=tv[0:5]
ch=dict(zip(tv,ch))
headers2={'Cookie':'UM_distinctid=16b6ddeef9031a-0fd2087250ae87-6353160-1fa400-16b6ddeef91978; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; u_t_0dfbd5c4476a8ffe3f02aca767156e5c=852682a2-c88d-4c34-a81a-23c46d7dcdaf; u_t_96b1a867d8603de2e0829a56fd89105f=956de084-0bb6-4a22-bbd3-ffff42096ca2; JSESSIONID=5E5D7D7690024A478B4AF3A9FAE47D8E; CNZZDATA1261166255=576782448-1560913678-null%7C1560918805','Referer':'http://www.yzntv.com/','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
for n,u in ch.items():
    r=geturl(u,headers=headers2)
    #print(r)
    playurl=re.findall(r'(http://yztv.+?),',r)
    playurl=playurl[0]
    print(n,playurl)