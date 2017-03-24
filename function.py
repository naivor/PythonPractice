#!/usr/bin/env python3
# -*- coding:utf-8 _*_

def  fun(x):
	if x>0:
		return x
	else:
		return -x

print(fun(-100))


def power(x,n=2):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s

print(power(10))
print(power(10,3))
	
	
