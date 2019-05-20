import base64
import re
'''
Servers=base64.b64decode(b'eyJsaXN0IjpbeyJpcCI6Imd3LnpoYW5xaS50diIsInBvcnQiOjE1MDEwLCJjaGF0cm9vbV9pZCI6MX0seyJpcCI6Imd3LnpoYW5xaS50diIsInBvcnQiOjE1MDEwLCJjaGF0cm9vbV9pZCI6MX0seyJpcCI6Imd3LnpoYW5xaS50diIsInBvcnQiOjE1MDEwLCJjaGF0cm9vbV9pZCI6MX1dfQ==')
print(Servers)
'''
def zqbsurl(streamUrl=''):
    VideoLevels=streamUrl
    url=base64.b64decode(VideoLevels)
    url=re.findall(r'http.+?m3u8',str(url))
    url=url[0].replace('\\','').replace('https','http')
    return url

a="\u5207\u5c14\u8bfa\u8d1d\u5229"#.\u5267\u60c5\u5143\u7d20"#'.Elements.of.Chernobyl.S01E01.\u4e2d\u82f1\u5b57\u5e55.WEBrip.720P-\u4eba\u4eba\u5f71\u89c6.mp4"
#y=a.encode('utf-8').decode('unicode_escape')
print(a)