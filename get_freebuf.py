# -*- coding:utf-8 -*-
import requests
import time

headers = {"Connection": "close",
"Cache-Control":"max-age=0",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,und;q=0.5"
}

proxies = {"http": "127.0.0.1:1080", "https": "127.0.0.1:1080"}

def go(): 
	f = open('freebuf.html','w')
	for num in range(1,470):
		url = "https://www.freebuf.com/articles/page/%s" % num
		s = requests.session()
		if num%2==0:
			print u"正在爬取第%s页中..." % num
			res = s.get(url,headers=headers)
		else:
			print u"正在爬取第%s页中..." % num
			res = s.get(url,headers=headers,proxies=proxies)	
		f.write(res.content)
		if (num-10)%20==0:
			time.sleep(480)
	f.close

if __name__ == '__main__':
	go()
