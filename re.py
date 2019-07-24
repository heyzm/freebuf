# -*- coding:utf-8 -*-
import re
import urllib
import io

url=''
title=''
time=''
tag = ''

def go():
	f = open('freebuf.txt')
	result = open('result.list','w')
	count = 0
	for line in f:
		if "<div class=\"news-img\"><a target=\"_blank\" href=\"" in line:
			url = "url:".join(re.findall(r"<div class=\"news-img\"><a target=\"_blank\" href=\"(.+?)\"><img calss",line))
			title = "title:".join(re.findall(r"title=\"(.+?)\" ",line))
			#title = urllib.unquote(title).decode("utf-8",'ignore').encode("gbk",'ignore')
			count=count+2
		if "<span class=\"time\">2" in line and count>0:
			time = "time:".join(re.findall(r"\t\t\t<span class=\"time\">(.+?)</span>",line))
			count = count-1
		if "<a href=\"https://www.freebuf.com/./" in line and count>0:
			tag = "tag:"
			if '</a><a' in line:
				tags = re.findall(r"\">(.+?)</a>",line)
			else:
				tags = re.findall(r"<a href=\"https://www\.freebuf\.com/\./.*\">(.+?)</a>",line)
			for temp in tags:
				tag = tag+temp+'、'
			#tag = urllib.unquote(tag[:-1]).decode("utf-8",'ignore').encode("gbk",'ignore')
			count =count-1
		#	print url+'   '+title+'    '+time+'    '+tag
			result.write(urllib.unquote(url+'   '+title+'    '+time+'    '+tag))
			result.write('\n')
			#result.write(url+'   '+urllib.unquote(title).decode("utf-8",'ignore').encode("gbk",'ignore')+'    '+time+'    '+urllib.unquote(tag).decode("utf-8",'ignore').encode("gbk",'ignore'))
#	result.close		
if __name__ == '__main__':
	go()

	#<div class="news-img"><a target="_blank" href="