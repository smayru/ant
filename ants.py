#p23
import numpy as np

L=10
n=3
X=np.array([2,6,7])

def test(L,n,X): 
	distance_max=np.empty(n)
	distance_min=np.empty(n)
	for i in range(n):

		if X[i]>=L-X[i]:
			distance_max[i]=X[i]
			distance_min[i]=L-X[i]
		else:
			distance_min[i]=X[i]
			distance_max[i]=L-X[i]
	time_min=np.min(distance_min)
	time_max=np.max(distance_max)
	print('min time ',time_min)
	print('max time ',time_max)
	return [distance_min,distance_max]

if __name__ == '__main__':
	test(L,n,X)
