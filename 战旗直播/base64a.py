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
    url=url[0].replace('\\','')
    return url
'''
cdns=base64.b64decode(b'eyJ2ZXIiOiIzLjAiLCJ2aWQiOiI0OTQyN19qbUFDSiIsInN0YXR1cyI6NCwibGluZSI6WyJcdTRlM2JcdTdlYmYiLCJcdTU5MDdcdTdlYmYxIiwiXHU1OTA3XHU3ZWJmMiIsIlx1NmQ3N1x1NTkxNiJdLCJyYXRlIjpbIlx1NTM5Zlx1NzUzYiIsIlx1OGQ4NVx1NmUwNUhEIiwiXHU4ZDg1XHU2ZTA1IiwiXHU5YWQ4XHU2ZTA1IiwiXHU2ODA3XHU2ZTA1Il0sInNxdWFyZSI6W1swLDAsNzIsNzIsNzJdLFswLDAsMjQyLDI0MiwyNDJdLFswLDAsMTIsMjQyLDI0Ml0sWzAsMCw3Miw3Miw3Ml1dLCJzdWZmaXgiOlsiIiwiXzcyMHBoZCIsIiIsIl80ODBwIiwiXzM2MHAiXSwicmF0ZUluZGV4IjoyLCJsb2NhbEZpcnN0IjoxLCJfdCI6InRhc2tfMSIsInJldmlldyI6MTczfQ==')
print(cdns)

h5Cdns=base64.b64decode(b'eyJ2ZXIiOiIzLjAiLCJ2aWQiOiI0OTQyN19qbUFDSiIsInN0YXR1cyI6NCwibGluZSI6WyJcdTRlM2JcdTdlYmYiLCJcdTU5MDdcdTdlYmYxIiwiXHU1OTA3XHU3ZWJmMiIsIlx1NmQ3N1x1NTkxNiJdLCJyYXRlIjpbIlx1NTM5Zlx1NzUzYiIsIlx1OGQ4NVx1NmUwNUhEIiwiXHU4ZDg1XHU2ZTA1IiwiXHU5YWQ4XHU2ZTA1IiwiXHU2ODA3XHU2ZTA1Il0sInNxdWFyZSI6W1swLDAsMjAyLDIwMiwyMDJdLFswLDAsNzIsNzIsNzJdLFswLDAsMjAyLDIwMiwyMDJdLFswLDAsMTcyLDE3MiwxNzJdXSwic3VmZml4IjpbIiIsIl83MjBwaGQiLCIiLCJfNDgwcCIsIl8zNjBwIl0sInJhdGVJbmRleCI6MiwibG9jYWxGaXJzdCI6MSwiX3QiOiJ0YXNrXzAiLCJyZXZpZXciOjE3M30=')
print(h5Cdns)
'''