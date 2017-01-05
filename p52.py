#p52

import numpy as np

n=4
w=[2,1,3,2]
v=[3,2,4,2]
W=5

def test(n,w,v,W):
	dp=np.zeros([n+1,W+1])-1
	dp[0::]=0
	for i in range(n):
		for j in range(W+1):
			if j< w[i]:
				dp[i+1,j]=dp[i,j]
			else:
				dp[i+1,j]=max(dp[i,j],dp[i,j-w[i]]+v[i])
	print(dp[n,W])


if __name__ == '__main__':
	test(n,w,v,W)
