#p66
import numpy as np

n=4
m=3
M=10000

def test(n,m,M):
	dp=np.zeros([m+1,n+1])
	dp[0,0]=1
	for i in range(1,m+1):
		for j in range(n+1):
			if (j-i>=0):
				dp[i,j]=(dp[i-1,j]+dp[i,j-i])%M
			else:
				dp[i,j]=dp[i-1,j]
	print(dp[m,n])

if __name__ == '__main__':
	test(n,m,M)
