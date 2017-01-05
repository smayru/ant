#49

import numpy as np

N=3
L=[8,5,8]

def test(N,L):
	cost=0
	tmp_L=L
	for i in range(N-1):
		sort_L=sorted(tmp_L)
		min_L=sort_L[0]
		second_L=sort_L[1]
		cost+=min_L+second_L
		tmp_L=sort_L[2::]
		tmp_L.append(min_L+second_L)
	print(cost)



if __name__ == '__main__':
	test(N,L)

