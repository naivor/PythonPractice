#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def upperFirst(s):
	if isinstance(s,str):
		return  upper(s[0])+lower(s[1-s.len():])


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(upperFirst, L1))
print(L2)

