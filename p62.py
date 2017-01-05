#p62
import numpy as np

n=3
a=[3,5,8]
m=[3,2,2]
K=17

def test(n,a,m,k):
	dp=np.zeros([n+1,K+1])-1
	dp[0,0]=0
	dp[1::,0]=m
	for i in range(n):
		for j in range(K+1):
			if dp[i,j]>=0:
				dp[i+1,j]=m[i]
			elif j<a[i] or dp[i+1,j-a[i]]<=0:
				dp[i+1,j]=-1
			else:
				dp[i+1,j]=dp[i+1,j-a[i]]-1
	if dp[n,K]>=0:
		print('yes')
	else:
		print('no')
if __name__ == '__main__':
	test(n,a,m,K)
