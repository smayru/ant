#p37
import numpy as np
from Queue import Queue

x=np.array([[1,0,1,1,1],[1,0,1,1,0],[1,0,1,0,0],[1,0,0,0,0],[1,1,1,1,0]])
start_x=0
start_y=1
goal_x=4
goal_y=4

def test(x,start_x,start_y,goal_x,goal_y):
	dx=np.array([1,0,-1,0])
	dy=np.array([0,1,0,-1])
	inf=100000
	mat=np.zeros([x.shape[0],x.shape[1]])+inf

	q = Queue()

	q.put([start_x,start_y])
	mat[start_x,start_y]=0

	while q.qsize()!=0:
		tmp=q.get()
		if tmp[0]==goal_x and tmp[1]==goal_y:
			print('clear')
			break
		else:
			for i in range(4):
				nx=tmp[0]+dx[i]
				ny=tmp[1]+dy[i]
				if (0<= nx and nx<x.shape[0] and 0<= ny and ny< x.shape[1] and x[nx,ny]==0 and mat[nx,ny]==inf):
					q.put([nx,ny])
					mat[nx,ny]=mat[tmp[0],tmp[1]]+1
	if mat[goal_x,goal_y]!=inf:
		print('clear')
	else: 
		print('no clear')

if __name__ == '__main__':
	test(x,start_x,start_y,goal_x,goal_y)
