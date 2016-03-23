#!/usr/bin/python


def insertSort(a):
	l = len(a)
	if l < 1:
		return []
	for i in range(1,l):
		if a[i-1] <= a[i]:
			continue
		else:
			temp = a[i]
			j = i
			while j > 0 and a[j-1] > temp:
				a[j] = a[j-1]
				j -= 1
			a[j] = temp
	return a


if __name__=='__main__':
	a = range(0,30)
	import random
	random.shuffle(a)
	print a
	print insertSort(a)
