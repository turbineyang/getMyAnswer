import  base64, os, time
from PIL import Image

start = time.time()
# 获取图片
os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.png")
os.system("adb pull /sdcard/screenshot.png G:\screenshot.png")

# 调用接口
host = 'https://ocrapi-ugc.taobao.com'
path = '/ocrservice/ugc'
method = 'POST'
appcode = '6c936c9cbfe84eabb6df40118da66fd1'
bodys = {}
url = host + path

# 裁剪
im = Image.open("G:\screenshot.png")
img_size = im.size
w = im.size[0]
h = im.size[1]
region = im.crop((70, 200, w - 70, 700))
region.save("g:/crop_test.png")
f = open('g:/crop_test.png', 'rb')
ls_f = base64.b64encode(f.read())
f.close()
s = bytes.decode(ls_f)

# 文本识别
header = {'Authorization': 'APPCODE ' + appcode, 'Content-Type': 'application/json; charset=UTF-8'}
bodys = {"img": s, "prob": "false"}
import requests

response = requests.post(url, json=bodys, headers=header)
result = response.json()
result = ''.join([i['word'] for i in response.json()['prism_wordsInfo']])
keyword = result.split('?')[0]  # 获得题目
print(keyword + '\n')

# 百度答案
bd_ulr = "https://www.baidu.com/s?wd=" + keyword

r = requests.get(bd_ulr, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"})

from lxml import etree

res = etree.HTML(r.text).xpath('//div[@class="c-abstract"]/text()')
for i in res[:]:
    print(i)

end = time.time()
print("共耗时：", end - start)
