#!/usr/bin/python


def bubbleSort(a):
	l = len(a)
	for i in range(l,0,-1):
		for j in range(0,i-1):
			if a[j] > a[j+1]:
				a[j],a[j+1] = a[j+1],a[j]
	return a


if __name__=='__main__':
	a = range(0,30)
	import random
	random.shuffle(a)
	print a
	print bubbleSort(a)
