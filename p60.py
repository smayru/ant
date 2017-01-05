#P60

import numpy as np

n=4
w=[2,1,3,2]
v=[3,2,4,2]
W=5

def test(n,w,v,W):
	dp=np.zeros([n+1,max(w)*max(v)])
	dp[0,:]=100
	dp[0,0]=0
	for i in range(n):
		for j in range(max(w)*max(v)):
			if j-v[i]<0:
				dp[i+1,j]=dp[i,j]
			else:
				dp[i+1,j]=min(dp[i,j],dp[i,j-v[i]]+w[i])
	dp[n::]
	tmp=0
	for i in range(max(w)*max(v)):
		if dp[n,i]<=W:
			tmp=i
	print(tmp)

if __name__ == '__main__':
	test(n,w,v,W)
