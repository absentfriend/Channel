#南宁
from requestget import geturl
import re
urlnn='http://app.nntv.cn/api/tt_live.php?type=1' \
      'http://app.nntv.cn/api/tt_live.php?type=1'
header1={'User-Agent': 'LuaSocket 3.0-rc1'}
r=geturl(urlnn)
n1=re.findall(r'http:\\/\\/m3u8.nntv.cn.+?.m3u8',r)
id=re.findall(r'"id":"[0-9]{7}',r)
for x in id:
    n=id.index(x)
    i=x.replace('"id":"','')
    n1[n]=n1[n].replace('\\','')
    print(n1[n])
    r = geturl(n1[n])
    print(r)
    ts=re.findall(r'/cutvlive/streams/events/.+?ts',r)
    for t in ts:
        ts[ts.index(t)]='http://m3u8.nntv.cn'+t
    print(i,ts)
#   rtmp://180.141.89.20/live/HXTV横县电视台     rtmp://180.141.89.20/live/MSTV马山电视台
