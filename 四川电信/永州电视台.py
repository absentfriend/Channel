#encoding:utf-8
from requestget import geturl
from lxml import etree
import requests
import re
#ch={'重庆卫视':'7','cqtv新闻':'9','cqtv影视':'194','cqtv都市':'198','重庆时尚':'206','文体娱乐':'200','公共农村':'208','重庆少儿':'210','重庆科教':'196','生活咨询':'202','重庆移动':'204','睛彩重庆':'633','ctv手持电视':'35','重庆国际':'637','重庆党员教育':'669','开州综合频道':'268','巴南综合频道':'276','大足综合频道':'286','綦江综合':'290','南山新闻综合':'298','丰都综合频道':'319','垫江综合频道':'329','14长寿频道':'188','铜梁综合频道':'248','巫溪综合频道':'337','忠县综合频道':'341','奉节综合频道':'347','秀山综合频道':'353','武隆综合频道':'357','沙坪坝新闻频道':'371','璧山综合频道':'411','万州综合频道':'232','yzzh':'258','yzsh':'260'}
ch={'重庆卫视':'7','cqtv新闻':'9','yzzh':'258','yzsh':'260'}
#綦江qi jiang
for x,y in ch.items():
 url='http://mapi.cbg.cn/live/detail?id='+y+'&redirectUrl=http://mapi.cbg.cn/live/list/sbcms?countyId=129'
 #url='http://mapi.cbg.cn/live/detail?id='+y+'&redirectUrl=http://mapi.cbg.cn/live/list/cqweb'
 #    http://mapi.cbg.cn/live/detail?id=198&redirectUrl=http://mapi.cbg.cn/live/list/cqweb
 headers={'User-Agent':'Mozilla/5.0 (Linux; Android 7.1.2; PIXEL 2 XL Build/NOF26V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Safari/537.36 Appbyme','Referer': 'wdcid=5a876f37950e0f79; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; wdses=642e981e4db045d4; qxsession=eyJpdiI6Im1WR2FERkZKNWs0b243amVhYnRwOVE9PSIsInZhbHVlIjoiczRlNDY1VEg4U1M0cWMrclJCMG5aU2l3d1pTV0dnUmVKYWVrNEFIeW56b2EwSnhJTHZJWXhKTjdoZlRSdm5hZVZFaGhIdW9MMXlJNGZTQ20zeTZ2YWc9PSIsIm1hYyI6ImFjZWQ4M2JlYWYwZmE3NDVkMzk5OGY2YzRkZDllNjEzODY1OTllMGE2OTE0MTAxYWI0ZGFjNWQ1NGVmYzlhMDkifQ%3D%3D; wdlast=1558942392'}
 # [truncated]Cookie: wdcid=0b370c8ca287de74; qxsession=eyJpdiI6IlJ2M2hHYlwvbzI4Mnc0c2dEXC9sOFNwUT09IiwidmFsdWUiOiJQU1gwZGJ0WlBLN2p5dFJNZkFNMHRzYzhrUDh0cGQyS082ZUxzcjZ3WW9WRDRZd05FZVJ1N1NnQUVFc2o0NXVZT2pIOTZrUGlpQkNEc0hEVW9qWUhIUT09IiwibWFj
 r=requests.get(url,headers=headers)
 r =geturl(url,headers=headers)
 print(r)
 '''
 html = etree.HTML(r.text)
 playurl=html.xpath('//video[@controls="controls"]/@src')
 '''
 playurl=re.findall('(http.+?)"',r)
 if playurl==[]:
  playurl='http://tx2play1.douyucdn.cn/live/218859rp1ftWXAUj_4000p.flv'
 else:
  playurl= playurl[1]
 print(x,playurl)