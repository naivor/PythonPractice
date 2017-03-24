#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def str2float(s):
	def num(s):
		return{"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,".":0.1}[s]

	def real(x,y):
		if y<0:
		
