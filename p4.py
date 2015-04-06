#!/usr/bin/env python
from decimal import Decimal
import math
def v(d1,d2):
	rate = d1/d2
	return rate

def v1(d1,d2):
	rate = d1//d2
	return rate
print v(1,2)
print v(1.0,2)
dec=Decimal(.1)
print dec
