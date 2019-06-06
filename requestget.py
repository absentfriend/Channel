import requests
headers = {'Referer': 'http://m.91kds.org/jiemu_sdqdtv1.html',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
def geturl(url,headers):
    r=requests.get(url,headers=headers)
    r.encoding='utf-8'
    #r.encoding='GB2312'
    r=r.text
    #print(r)
    return r

def posturl(url,data):
    headers = {'Referer': 'http://m.91kds.org/jiemu_sdqdtv1.html',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    r=requests.post(url,json=data,headers=headers)
    r.encoding='utf-8'
    #r.encoding='GB2312'
    r=r.text
    #print(r)
    return r
