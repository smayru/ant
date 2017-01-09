#p80
import numpy as np
import unionfind

N=100
K=7
T=[1,2,2,2,1,2,1]
X=[101,1,2,3,1,3,5]
Y=[1,2,3,3,3,1,5]

def test(N,K,T,X,Y):
	ans=0
	u = unionfind.unionfind(3*N)
	for i in range(K):
		t=T[i]
		x=X[i]-1
		y=Y[i]-1
		if t==1:
			if (u.issame(x, y+N) or u.issame(x, y+N))==True:
				ans+=1
			else:
				u.unite(x,y)
				u.unite(x+N,y+N)
				u.unite(x+N*2,y+N*2)
		elif t==2:
			if (u.issame(x, y) or u.issame(x, y+2*N))==True:
				ans+=1
			else:
				u.unite(x,y+N)
				u.unite(x+N,y+2*N)
				u.unite(x+N*2,y)
	print(ans)
if __name__ == '__main__':
	test(N,K,T,X,Y)


