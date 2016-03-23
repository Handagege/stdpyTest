#!/usr/bin/python


def mergeSort(a):
	mi = len(a)/2
	if len(a) > 2:
		return merge(mergeSort(a[0:mi]),mergeSort(a[mi:len(a)]))
	else:
		return merge(a[0:mi],a[mi:len(a)])


def merge(a,b):
	i,j,z = len(a)-1,len(b)-1,len(a)+len(b)
	mergeResult = [0]*z
	while i > -1 and j > -1:
		z -= 1
		if a[i] > b[j]:
			mergeResult[z] = a[i]
			i -= 1
		else:
			mergeResult[z] = b[j]
			j -= 1
	if i == -1:
		for index in range(j+1):
			mergeResult[index] = b[index]
	else:
		for index in range(i+1):
			mergeResult[index] = a[index]
	return mergeResult


if __name__=='__main__':
	a = range(0,30)
	import random
	random.shuffle(a)
	print a
	print mergeSort(a)
