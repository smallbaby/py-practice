#!/usr/bin/env python
for each in [1,2,3]:
	print each
for each in range(3):
	print each
foo="abc"
for c in foo:
	print c

print "===================="
for i,ch in enumerate(foo):
	print ch,'(%d)' % i
print "#########################"
a=[x**2 for x in range(4) if not x%2]
for i in a:
	print i
try:
	print 1/0
except:
	print "H"
def addMe2Me(x=2):
	return x+x
print addMe2Me('python')
print addMe2Me([-1,'abc'])
print addMe2Me()

print "##################################While#####################"

i=0
while(i<=10):
	print i
	i+=1
for i in range(0,11):
	print i
print "##########################IF####################"
num=raw_input("Enter a number:")
num=int(num)
print "num===",num
if num < 0:
	print "fushu"
elif num > 0:
	print "zhengshu"
else:
	print "num=0"
print "#########################FOR STRING ###############"
str="zhangkai"
for b in str:
	print b
