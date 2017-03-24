#!/usr/bin/env  python3
# -*- coding:utf-8 -*-

def is_palindrome(n):
	str_n=str(n)
	if len(str_n)<3:
		return False
	n_str=str_n[::-1]
	return n_str==str_n

output = filter(is_palindrome, range(1, 1000))
print(list(output))
		
	
