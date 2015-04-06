#!/usr/bin/env python
#coding=utf-8
import re
import urllib

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html
def downloadImg(html):
	reg = r'src="(.+?\.jpg)" pic_ext'
	imgre = re.compile(reg)
	imgList = re.findall(imgre, html)
	for i,url in enumerate(imgList):
		urllib.urlretrieve(url,'%s.jpg' % (i,))

html = getHtml("http://tieba.baidu.com/p/3558925045")
getImg(html)
