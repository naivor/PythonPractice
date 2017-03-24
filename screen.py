#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Screen(object):
	
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self,value):
		self._width=value

	@property
	def height(self):
		return self._height
	@height.setter
	def height(self,value):
		self._height=value
	@property
	def resolution(self):
		return self._width*self._height
	def __init__(self):
		self.n=0
	def __iter__(self):
		return self
	def __next__(self):
		self.n=self.n+1
		if self.n>10:
			raise StopIteration()
		return self.n
	def __getitem__(self,n):
		
		i=0

		if isinstance(n,int):
			for x in range(n):
				i=i+1
			return i

		if isinstance(n,slice):
			start=n.start
			stop=n.stop
			if start==None:
				start=0
			L=[]
			for x in range(stop):
				if x>=start:
					L.append(i)				
				i=i+1
			return L

s=Screen()
s.width=100
s.height=150

print(s.width,s.height,s.resolution)

for n in Screen():
	print(n)	


print(Screen()[10])
print(Screen()[5:10])
