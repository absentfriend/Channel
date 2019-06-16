from MD5 import get_token
import requests
from requestget import  geturl
from requestget import posturl
from DPL频道列表模板 import lists
import re
import os
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36','Referer':'http://www.cbg.cn/live/Index.shtml','Host':'app.cbg.cn','X-Requested-With':'ShockwaveFlash/22.0.0.192'}
ch={'汽摩':'5','新闻':'3','时尚':'17','科教':'9','生活':'12','都市':'10','少儿':'19','移动':'16','娱乐':'11','影视':'6','农村':'18','手持电视':'20'}
playurls=[]
for x,id in ch.items():
    url='http://app.cbg.cn/?app=activity&controller=wwsp&action=hlive_md5&callback=jQuery_&ch=%2Fapp_2%2F_definst_%2Fls_'+id+'.stream%2Fchunklist.m3u8&_='
    r=geturl(url,headers=headers)
    print(r)
    url1='http://sjlivecdnx.cbg.cn/1ive/stream_'+id+'.php'
    requests.get(url1,headers)
    playurl=re.findall('http.+?m3u8',r)
    playurl=playurl[0].replace('\\','')
    r1=geturl(url1,headers=headers)
    #print(r1)
    playurls.append(playurl)
names=list(ch.keys())
with open('cqtv.dpl', 'w', encoding="utf-8") as f: f.write('')
with open('cqtv.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0\n')
for u in playurls:
    j=playurls.index(u)
    (x,y)=lists(names[j],u)
    with open('cqtv.dpl', 'a+', encoding="utf-8") as f: f.write(str(j+1)+x + "\n"+str(j+1)+y+"\n"+str(j+1)+'*played*0\n')
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\重庆电视\\cqtv.dpl')
