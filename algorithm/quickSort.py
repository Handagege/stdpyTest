#!/usr/bin/python

def partition(a,start,end):
	small = start - 1
	for index in range(start,end):
		if a[index] < a[end]:
			small += 1
			if small != index:
				a[small],a[index] = a[index],a[small]
	small += 1
	a[small],a[end] = a[end],a[small]
	return small


def quickSort(a,start,end):
	if start == end:
		return
	index = partition(a,start,end)
	if index > start:
		quickSort(a,start,index-1)
	if index < end:
		quickSort(a,index+1,end)


if __name__=='__main__':
	a = range(0,30)
	import random
	random.shuffle(a)
	print a
	quickSort(a,0,len(a)-1)
	print a
