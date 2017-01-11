#p103
import numpy as np
import unionfind

N=5
M=5
R=8

x=[4,1,0,0,3,1,4,2]
y=[3,3,0,1,3,3,2,2]
d=[6831,4583,6592,3063,4975,2049,2104,781]

#############################################
#############################################
V=N+M
E=R
d=-1*np.array(d)
x=np.array(x)
y=np.array(y)
def kruskal(x,y,d,V,E):
	u = unionfind.unionfind(N+M)
	tmp_d=np.sort(d)
	x=x[np.argsort(d)]
	y=y[np.argsort(d)]
	res=0
	for i in range(E):
		e=tmp_d[i]
		if (u.issame(x[i], y[i]+N)==False):
			u.unite(x[i], y[i]+N)
			res+=e
	return res

def test():
	print(V*10000+kruskal(x,y,d,V,E))

if __name__ == '__main__':
	test()