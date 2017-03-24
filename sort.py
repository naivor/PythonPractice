#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import Iterable

def by_name(t):
	if isinstance(t,Iterable):
		return t[0]
	else:
		return t

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name)
print(L2)
