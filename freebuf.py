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

def go(): 
	f = open('free_vuls','w')
	for num in range(1,98):
		url = "https://www.freebuf.com/vuls/page/%s" % num
		s = requests.session()
		res = s.get(url,headers=headers)
		f.write(res.content)
		if num%10==0:
			time.sleep(480)
	f.close

if __name__ == '__main__':
	go()
