#p73
import numpy as np
import Queue

N=4
L=25
P=10
A=[10,14,20,21]
B=[10,5,2,4]

def test(N,L,P,A,B):
	ans=0
	pos=0
	tank=P

	q=Queue.PriorityQueue()
	for i in range(N):
		d=A[i]-pos
		while tank-d<0:
			if q.empty()==True:
				print('-1')
				break
			tank+=-1*q.get()
			ans+=1
		tank-=d
		pos=A[i]
		q.put(-1*B[i])
	print(ans)
if __name__ == '__main__':
	test(N,L,P,A,B)
