#p102
import numpy as np

N=4
R=4
G=[[1],[0,2,3],[1,3],[1,2]]

inf=100000
cost=np.zeros([N,N])+inf
cost[0,1]=100
cost[1,2]=250
cost[1,3]=200
cost[2,3]=100
cost[1,0]=100
cost[2,1]=250
cost[3,1]=200
cost[3,2]=100

def test(N,R,inf,cost):

	dist=np.zeros([N])+inf
	dist2=np.zeros([N])+inf
	used=[False]*N
	used2=[False]*N
	dist[0]=0

	while True:
		v=-1
		for  u in range(N):
			if used[u]!=True and (v==-1 or dist[u]<dist[v]):
				v=u
		if v==-1:
			break

		used[v]=True
		for u in range(N):
			dist[u]=min(dist[u],dist[v]+cost[v,u])

	while True:
		v=-1
		for  u in range(N):
			if used2[u]!=True and (v==-1 or dist2[u]<dist2[v]):
				v=u
		if v==-1:
			break

		used2[v]=True
		for u in range(N):
			for j in range(N):
				if dist[u]!=dist[j]+cost[j,u]:
					dist2[u]=min(dist2[u],dist2[j]+cost[j,u],dist[j]+cost[j,u])
				else:
					dist2[u]=min(dist2[u],dist2[j]+cost[j,u])
	print(dist2[N-1])
if __name__ == '__main__':
	test(N,R,inf,cost)

