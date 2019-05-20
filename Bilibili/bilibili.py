#http://live.bilibili.com/api/playurl?player=1&quality=0&platform=android&otype=json&cid=11735834
#http://js.live-play.acgvideo.com/live-js/452244/live_172925919_1966898.flv?wsSecret=b0886973c9a9618b5775605bcc6a59a8&wsTime=1557287965&trid=539b9b6ebbcd4901a6531d01762f596b&order=1&sig=no
from requestget import geturl
import re
import requests
import json
import jsonpath
import os
from DPL频道列表模板 import lists
headers={'Cookie':'buvid3=4548AA72-6BE9-4943-A309-00DF76CF27D0110247infoc; LIVE_BUVID=AUTO8915583204905357; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1558320496; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1558321289; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1','Host':'live.bilibili.com','Referer': 'https://live.bilibili.com/all?visit_id=bthwzr7gxu80','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7'}
titles=[]
roomids=[]
for n in range(1,11):
    url='http://api.live.bilibili.com/room/v3/area/getRoomList?platform=web&parent_area_id=1&cate_id=0&area_id=33&sort_type=income&page='+str(n)+'&page_size=30&tag_version=1'
    #r=geturl(url,headers=headers)
    r=requests.get(url)
    #print(r.text)
    dictinfo = json.loads(r.text)
    #print(dictinfo)
    d=list(dictinfo['data'].values())
    dl=d[1]
    for i in dl:
        roomid=i['roomid']
        title=i['title']
        if title=='　':
            title='AAAA'
        roomids.append(roomid)
        titles.append(title)
dic=dict(zip(titles,roomids))
playurls=[]
for x,y in dic.items():
    #print(x,y)
    url='https://live.bilibili.com/'+str(y)
    r=geturl(url,headers=headers)
    playurl=re.findall('url":"(.+?)"',r)
    playurl=playurl[3].encode('utf-8').decode('unicode_escape')
    playurls.append(playurl)
    print(x,playurl)
with open('B站直播.dpl', 'w', encoding="utf-8") as f: f.write('')
with open('B站直播.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0\n')
for u in playurls:
    j=playurls.index(u)
    (x,y)=lists(titles[j], u)
    with open('B站直播.dpl', 'a+', encoding="utf-8") as f: f.write(str(j + 1) + x + "\n" + str(j + 1) + y + "\n" + str(j + 1) + '*played*0\n')
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\Bilibili\\B站直播.dpl')