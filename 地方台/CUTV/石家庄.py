from requestget import geturl
import json
ch={'石家庄新闻':'2','石家庄娱乐':'3','石家庄生活':'4','石家庄都市':'5'}
for x,y in ch.items():
    url='http://mobile.sjzntv.cn/app/channel_detail.php?appid=8&appkey=BJaFDrsqqZQelNRXE6EhUXmlfzhq5Rox&device_token=6b07de2166a86e9dbbfb570268574467&_member_id=&version=2.0&app_version=2.0&app_version=2.0&package_name=com.hoge.android.app.wxsjz&system_version=4.4.4&phone_models=VAY_32MOS&ad_group=mobile&channel_id='+y
    r=geturl(url)
    r=json.loads(r)
    playurl=r[0]['m3u8']
    print(playurl)

