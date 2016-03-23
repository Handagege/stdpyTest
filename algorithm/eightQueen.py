#!/usr/bin/python


def check(a,n):
	for i in range(0,n):
		if a[i] == a[n] or abs(a[i]-a[n]) == abs(i-n):
			return False
	return True


def printQueen(a,n):
	global resultNum
	resultNum += 1
	print '\n'
	print 'case ' + str(resultNum) + ' : '
	q = []
	for i in range(0,n):
		b = ['.']*n
		q.append(b)
	for i in range(0,n):
		q[i][a[i]] = 'Q'
	for i in q:
		print ' '.join(i)


def queen(a,n,r):
	if r == n:
		printQueen(a,n)
	else:
		for i in range(0,n):
			a[r] = i
			if check(a,r):
				queen(a,n,r+1)


def queenNonCursion1(a,n,r):
	while r >= 0:
		if a[r] != n-1:
			for i in range(a[r]+1,n):
				a[r] = i
				if check(a,r):
					if r == n-1:
						printQueen(a,n)
					else:
						r += 1
						break
		else:
			a[r] = -1
			r -= 1


def queenNonCursion2(a,n,r):
	while r >= 0:
		if a[r] != n-1:
			while a[r] < n-1:
				a[r] += 1
				if check(a,r):
					if r == n-1:
						printQueen(a,n)
					else:
						r += 1
						a[r] = -1
						break
		else:
			r -= 1


def test1():
	import time
	n = 10
	beg = time.time()
	a = [-1]*n
	resultNum = 0
	queen(a,n,0)
	print 'recursion method cost time : {0:.3} '.format(time.time()-beg)
	beg = time.time()
	a = [-1]*n
	resultNum = 0
	queenNonCursion1(a,n,0)
	print 'non recursion method cost time : {0:.3} '.format(time.time()-beg)


if __name__ == '__main__':
	import time
	n = 8
	beg = time.time()
	a = [-1]*n
	resultNum = 0
	queenNonCursion2(a,n,0)
	print 'non recursion method cost time : {0:.3} '.format(time.time()-beg)




