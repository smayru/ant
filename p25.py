#p25
import numpy as np

n=3
m=10
k=[1,3,5]



def binary_search(x,kk):
	size_kk=kk.shape[0]
	left=0
	right=size_kk
	a=False
	while (right-left)>=1:
		current=(right+left)/2
		if kk[current]==x:
			a=True
			break
		elif kk[current]>x:
			right=current
		else:
			left=current
	return a
def test(n,m,k):
	kk=np.empty([n,n])
	for i in range(n):
		for j in range(n):
			kk[i,j]=k[i]+k[j]
	sort_kk=np.sort(kk.reshape(n*n))

	ans=False
	for i in range(n):
		for j in range(n):
			x=m-k[i]-k[j]
			if binary_search(x,sort_kk)==True:
				ans=True
	print(ans)

if __name__ == '__main__':
	test(n,m,k)

