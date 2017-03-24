#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def pp(func):
	def wrapper(*args,**kw):

		print('begin call %s()' % func.__name__)
		return func(*args,**kw)

	print(' end 1 call %s()' % func.__name__)
	return wrapper
	


@pp
def now():
	print("现在是晚8点")

f=now

print(f())

print(f.__name__)
