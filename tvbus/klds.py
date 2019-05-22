from requestget import geturl
from requestget import posturl
url='http://apiklds.clouddianshi.com:8882/BroadbandSaasH5/Video/channelList'
headers={'SAAS':'cn.grtech.tv','User-Agent':'okhttp/3.9.1','Content-Type':'application/json;charset=utf-8','Host':'apiklds.clouddianshi.com:8882'}
r=geturl(url,headers=headers)
print(r)

url2='http://apiklds.clouddianshi.com:8882/BroadbandSaasH5/Video/getRealUrl?uid=a23594f8-9b32-4671-9eb3-03f652cb17c6&type=1&userid=0&channelId=2'
r2=posturl(url2,data={},headers=headers)
print(r2)