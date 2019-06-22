from MD5 import get_token
import requests
from requestget import  geturl
from requestget import posturl
from DPL频道列表模板 import lists
import re
import os
#from lxml import etree
#http://www.cbg.cn/live/Index.shtml
#http://www.cbg.cn/live/Index.shtml
#http://www.cbg.cn/live/Index.shtml
#http://www.cbg.cn/live/lndex.shtml
urlr='http://www.cbg.cn/'
headers2={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36','Referer':'http://www.cbg.cn/live/lndex.shtml','Host':'app.cbg.cn','X-Requested-With':'ShockwaveFlash/22.0.0.192'}
ch={'汽摩':'5','新闻':'3','时尚':'17','科教':'9','生活':'12','都市':'10','少儿':'19','移动':'16','娱乐':'11','影视':'6','农村':'18','手持电视':'20'}
res = geturl(urlr,headers=headers2)
print(res)
for x,id in ch.items():
    url='http://app.cbg.cn/?app=activity&controller=wwsp&action=hlive_md5&callback=jQuery17208145252600791988_1560739117765&ch=%2Fapp_2%2F_definst_%2Fls_'+id+'.stream%2Fchunklist.m3u8&_=1560739124932'
    r=geturl(url,headers=headers)
    playurl=re.findall('http.+?m3u8',r)
    playurl=playurl[0].replace('\\','')
    print(x,playurl)
