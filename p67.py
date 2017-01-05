#p67
import numpy as np

n=3
m=3
a=[1,2,3]
M=10000

def test(n,m,a,M):
	dp=np.zeros([m+1,n+1])
	dp[:,0]=1
	for i in range(n):
		for j in range(1,m+1):
			if (j-1-a[i]>=0):
				dp[i+1,j]=dp[i+1,j-1]+dp[i][j]-dp[i][j-1-a[i]]
			else:
				dp[i+1,j]=dp[i+1,j-1]+dp[i,j]
	print(dp[m,n]%M)
if __name__ == '__main__':
	test(n,m,a,M)
