#!/usr/home/zhanghan5/anaconda3/bin/python

import numpy as np

def LCS(a,b):
	la = len(a)
	lb = len(b)
	dp = np.zeros([la+1,lb+1],int)
	for i in range(la):
		for j in range(lb):
			if a[i] == b[j]:
				dp[i+1][j+1] = dp[i][j] + 1
			else:
				dp[i+1][j+1] = dp[i][j+1] if dp[i][j+1] > dp[i+1][j] else dp[i+1][j]
	return dp


def printLCS(dp,a,i,j):
	if i == 0 or j == 0:
		return
	if dp[i-1][j] == dp[i][j-1]:
		if  dp[i-1][j] == dp[i-1][j-1] and dp[i-1][j-1] < dp[i][j]:
			printLCS(dp,a,i-1,j-1)
			print(a[i-1])
		else :
			printLCS(dp,a,i-1,j)
	else:
		printLCS(dp,a,i-1,j) if dp[i-1][j] > dp[i][j-1] else printLCS(dp,a,i,j-1)


if __name__ == '__main__':
	a = "bdcaba"
	b = "abcbdab"
	print(LCS(a,b).T)
	print('\n')
	printLCS(LCS(a,b),a,len(a),len(b))
		

