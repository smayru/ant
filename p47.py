#47
import numpy as np

N=6
R=10
X=[1,7,15,20,30,50]

def test(N,R,X):
	ans=np.zeros(N)
	p=0
	pos=0


	while pos<X[N-1]:
		if np.sum(ans)==0:
			for j in range(N):
				if X[j]>pos+R:
					pos=X[j-1]
					ans[j-1]=1
					p=i-1
					break
		else:
			for j in range(N):
				if X[j]>pos+R:
					pos=X[j]
					ans[j]=1
					break
	print(int(np.sum(ans)))

if __name__ == '__main__':
	test(N,R,X)
