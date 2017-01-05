#p58
import numpy as np

n=3
w=[3,4,2]
v=[4,5,3]
W=7

def test(n,w,v,W): 
	dp=np.zeros([n+1,W+1])
	dp[0,:]=0

	for i in range(n):
		for j in range(W+1):
			if j-w[i]<0:
				dp[i+1,j]=dp[i,j]
			else:
				dp[i+1,j]=max(dp[i,j],dp[i+1,j-w[i]]+v[i])
	print(dp[n,W])

if __name__ == '__main__':
	test(n,w,v,W)
