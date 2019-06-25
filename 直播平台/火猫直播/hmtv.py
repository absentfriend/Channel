from requestget import geturl
import re
import os
h={}
url='http://api.huomao.com/channels/channelDetail?an=10&cid=19294&now_time=1561438152&post_data=1&refer=androidTV&time=26023969&token=5cf9ceae8b38fb09610950c32dfbdfab&ver=1.9'
r=geturl(url,headers=h)
p=re.findall(r'TD":"(http:.+?)"',r)
for x in p:
    p[p.index(x)]=x.replace('\\','')
playurl=p[-2]
print(playurl)
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
