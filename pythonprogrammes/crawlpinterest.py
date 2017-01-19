import urllib.request
import re
import random

keyword="League%20of%20Legends"

uapools=[
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3",
    "Opera/8.0 (Macintosh; PPC Mac OS X; U; en)",
    "Mozilla/5.0 (iPhone; U; CPU like Mac OS X) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/4A93",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",
    ]
def ua(uapools):
    thisua=random.choice(uapools)
    print(thisua)
    opener=urllib.request.build_opener()
    headers=("User-Agent",thisua)
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)

opener=urllib.request.build_opener
headers=("User-Agent","Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)")
opener.addheaders=[headers]
url="https://www.pinterest.com/search/pins/?q="+keyword
data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
pat='"images": {"736x": {"url": "(.*?)"'
rst=re.compile(pat).findall(data)

for i in range(0,len(rst)):
    print("正在爬取第"+str(i)+"张图片")
    thislink=rst[i]
    file="F:\\只是文件夹\\编程\\LOLimg_pinterest\\LOLimage"+str(i)+".jpg"
    urllib.request.urlretrieve(thislink,filename=file)
