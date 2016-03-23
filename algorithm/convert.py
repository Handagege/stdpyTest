#!/usr/bin/python


from collections import deque


def convert(n,base):
	s = deque()
	while n > 0:
		s.appendleft(n%base)
		n = n / base
	return s



if __name__=="__main__":
	import random
	n = random.randint(0,10000)
	print n
	char = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
	result = convert(n,16)
	s = ""
	for i in result:
		s += char[i]
	print s
