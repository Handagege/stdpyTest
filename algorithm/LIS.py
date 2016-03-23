#!/usr/bin/python

import sys

def binarySearch(a,r,i):
	right = r
	left = 0
	while(left <= right):
		mid = (left+right)/2
		if a[mid] == i:
			return mid
		elif a[mid] < i:
			left = mid+1
		else:
			right = mid-1
	return left

def LIS(a):
	ans = [0]*len(a)
	ans[0] = a[0]  
	l = 0
	for index,value in enumerate(a):
		if value > ans[l]:
			l += 1
			ans[l] = value
		else:
			ans[binarySearch(ans,l,value)] = value
		print index,ans
	return ans


if __name__ == '__main__':
	a = [2,3,6,45,10,12,5,9,11,17,13,14,15]
	print LIS(a)
		

