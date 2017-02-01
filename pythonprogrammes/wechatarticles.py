

def ua_p(url):
    import random
    import urllib.request
    uapools=["Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
         "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
         "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"
         "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
         ]
    thisua=random.choice(uapools)
    print(thisua)
    headers=("User-Agent",thisua)
    #thisip="127.0.0.1:8888"
    #print("当前ip是"+thisip)
    #proxy=urllib.request.ProxyHandler({"http":thisip})
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    urllib.request.install_opener(opener) 

    data=urllib.request.urlopen(url).read()
    dataa=data.decode("utf-8","ignore")
    print(len(dataa))
    return dataa
    

import re
import urllib.request
key="python"
for i in range(0,10):
    key=urllib.request.quote(key)
    url="http://weixin.sogou.com/weixin?query="+key+"&type=2&page="+str(i+1)
    thispagedata=ua_p(url)
    print(len(thispagedata))
    pat='<div class="txt-box">.*?data-url="(.*?)"'
    rst=re.compile(pat,re.S).findall(thispagedata)
    for j in range(0,len(rst)):
        thisurl=rst[j]
        data2=ua_p(thisurl)
        print("当前爬取"+thisurl)
        fh=open("F:\\RST\\关于python文章"+str(i)+"-"+str(j)+".html","w",encoding="utf-8")
        fh.write(data2)
        fh.close()

