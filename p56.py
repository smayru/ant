#p56
import numpy as np

n=4
m=4
s="abcd"
t="becd"

def test(n,m,s,t):
	dp=np.zeros([n,m])

	for i in range(n):
		for j in range(m):
			if s[i]==t[j]:
				dp[i,j]=dp[i-1,j-1]+1
			else:
				dp[i,j]=max(dp[i,j-1],dp[i-1,j])
	print(int(dp[n-1,m-1]))

if __name__ == '__main__':
	test(n,m,s,t)

