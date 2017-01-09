#p75
import numpy as np
import Queue

N=3
L=[8,5,8]

def test(N,L):
	q=Queue.PriorityQueue()
	ans=0

	for i in range(N):
		q.put(L[i])
	while q.qsize()>1:
		tmp1=q.get()
		tmp2=q.get()
		ans+=tmp1+tmp2
		q.put(tmp1+tmp2)
	print(ans)

if __name__ == '__main__':
	test(N,L)
