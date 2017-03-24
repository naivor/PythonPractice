#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class  Student(object):

	def __init__(self,name,pwd):
		self.name=name
		self.pwd=pwd
	def __str__(self):
		return "Student (name:%s,pwd:%s)" %(self.name,self.pwd)




s1=Student("xiaoming","xxxxxx")

print(s1)

print(s1.name,s1.pwd)


class Seniour(Student):

	__slots__=("height","weight")
	
	def __str__(self):
		return "Seniour(height:%s,weight:%s)" % (self.height,self.weight)
	

s2=Seniour("xiaohua","bengdan")
s2.height=180
s2.weight=58
s2.age=28

print(s2)
print(s2.name,s2.pwd,s2.age,s2.height,s2.weight)
