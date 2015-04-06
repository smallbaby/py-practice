import numpy
def f_2(data,estimate):
	return sum(where(data!=0,(data-estimate)**2,0))

print f_2(4,2)
