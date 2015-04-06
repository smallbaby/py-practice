#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import re
########测试re模块##############
#1. 匹配单词
str="python"
pat="python"
print re.findall(pat,str)
'''
通配符：点.代表任意字符
转义加斜杠  xxx\\.jpg
字符集:使用中括号创建字符集[]，可以使用范围['a'-'z']匹配a-z的任意一个字符
[a-zA-Z0-9] 匹配任意大小写字母数字
反转： [^abc] 匹配除了a/b/c之外的字符
选择符：    ‘python|perl
子模式： 'p(python|perl)
可选，在子模式加？,不是必须匹配到
r'(http://?(www\.)?python\.org'
可以匹配到：
	www.python.org
	http://www.python.org
	python.org
	http://python.org
重复子模式
(xx)* >=0次 r'w*\.python\.org'   .python.org w.python.org wwwwww.python.org
(xx)+ >=1   r'w+\.python\.org   不能匹配.python.org
(xx){m,n} 重复m~n次 r'w{3,4}\.python\.org 只能匹配到 www.python.org wwww.pytxxx
re模块的内容
compile(pattern) 在字符串中找模式
search(pattern,string) 开始处匹配模式
	if re.search(pat,str) print "YES"

split(pattern,string) 分割字符串
findall(pat,str) 所有匹配项
sub(pat,rep,string) 替换
escape(str) 转义

'''
#split
text='app,ios,android,window,,,delta'
print "split::::::"
print re.split('[,]+',text)
#findall
pat='[a-zA-Z]+'
text='"Hm..err-- are you sure?" he said,sounding insecure.'
print "findall:::::"
print re.findall(pat,text)

#sub
pat='{name}'
text = 'Dear {name}....'
print re.sub(pat,'zhangkai',text)

print '###################################'
'''匹配对象和组
group start end span
'''
# www开头  中间任意字符 .后边为三个字符
m=re.match(r'www\.(.*)\..{3}','www.python.org')
print m.group()
print m.group(0)
print m.group(1)
'''
\d 数字
\D 非数字
\s 空白字符   a\sc a c
\S 非空       a\Sc  abc
\w 单词     a\wc abc
\W 非单词   a\Wc a c

*










'''


















