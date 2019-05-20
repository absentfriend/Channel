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