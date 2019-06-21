from requestget import geturl
from requestget import posturl
from MD5 import get_token
import requests
import time
import uuid
import hashlib
import md5hash
from 斗鱼直播.斗鱼接口 import  APIHelper
import re
header={'Referer':'https://m.douyu.com/9999',"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36','Origin':'https://m.douyu.com'}
t=str(int(time.time()))
rt=str(int(time.time()*1000))
#print(r1)
auth=get_token(message="room/"+'9999'+"?aid=ios&clientsys=ios&time="+t+'1231')
u1='http://www.douyutv.com/api/v1/room/'+'9999'+'?aid=ios&auth='+auth+'&client_sys=ios&time='+t
print(u1)
h={'Accept':'application/json, text/plain, */*','auth':auth,'Content-Type':'application/x-www-form-urlencoded','Origin':'https://www.douyu.com','Referer':'https://www.douyu.com/g_DOTA2','rid':'52876','time':rt,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
r=geturl(u1,headers=h)
print(r)
'''
s=>>> s = "string"
>>> l = list(s)
>>> l.sort()
>>> s = "".join(l)
'''
sign=get_token(message='api/room/ratestream'+t)
print(sign)
params ={'tt':'1561114109','did':'58c9702b21a690730fc9434b00011531','rid':'9999','v':'250120190621','sign':'53f33cf40bfb302f319e734c69823f02','ver':'219032101','rate':'3'}
print(sign)
u2='https://m.douyu.com/api/room/ratestream'
r2=requests.post(u2,data=params,headers=header)
r2.encoding = 'utf-8'
# r.encoding='GB2312'
r = r2.text
key=re.findall(r'live/(.+?)_',r)
key=key[0]
print(r)
playurl='http://tx2play1.douyucdn.cn/live/'+key+'_4000p.flv'
print(playurl)



'''
params ={'tt':'1561109493','did':'58c9702b21a690730fc9434b00011531','rid':'9999','v':'250120190621','sign':'5af1dc8ea555cd6301f17d7fd2099b7e','ver':'219032101','rate':'-1'}
r=requests.post(url,files=params,headers=h)
r.encoding = 'utf-8'
# r.encoding='GB2312'
r = r.text
'''

'''
def __init__(self):
    self.baseUrl = "http://www.douyutv.com/api/v1/"
    self.midReq = "?aid=android&cdn=ws&client_sys=android&time="

def GetStringMD5(self, str):
    m = md5hash.new()
    m.update(str)
    return m.hexdigest()
def request(self, action, param=None):
    t = str(int(time.time()))
    md5_url = action + self.midReq + t + "1231"
    auth = self.GetStringMD5(md5_url)
    return auth
'''