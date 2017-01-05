#p35
import numpy as np

x=np.array([[1,0,0,0,1],[0,1,1,0,1],[0,0,1,0,1],[0,0,0,0,1],[0,0,0,0,1]])
n=5
m=5

def dfs(i,j):
	x[i,j]=0
	for x1 in range(-1,2):
		for x2 in range(-1,2):
			dn=i+x1
			dm=j+x2
			if dn>=0 and dn<n and dm>=0 and dm<m and x[dn,dm]==1:
				return dfs(dn,dm) 

def test(n,m,x):
	res=0
	for i in range(n):
		for j in range(m):
			if x[i,j]==1:
				dfs(i,j)
				res+=1
	print(res)
if __name__ == '__main__':
	test(n,m,x)
