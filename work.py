#p43
import numpy as np
n=5
s=[1,2,4,6,8]
t=[3,5,7,9,10]


def test(s,t,n):
	s=np.array(s)
	t=np.array(t)
	mat=np.c_[s,t]
	mat = mat[ mat[:,1].argsort() ]

	res=0
	time=0
	for i in range(n):
		if time < mat[i,0]:
			time=mat[i,1]
			res+=1
	print(res) 
	return res

if __name__ == '__main__':
	test(s,t,n)

