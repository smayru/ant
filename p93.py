#p93
import numpy as np

n=4
G=[[1,3],[0,2],[1,3],[0,2]]

G=np.array(G)
color=np.zeros(n)

def dfs(v,c):
	global color
	color[v]=c
	a=True
	for i in range(len(G[v])):
		if color[G[v][i]]==c:
			a=False
		elif color[G[v][i]]==0 and dfs(G[v][i],-c)==False:
			a=False
	return a
def test(n,G):
	for v in range(n):
		if color[v]==0:
			if (dfs(v,1)!=True):
				print('No')
	print('yes')
if __name__ == '__main__':
	test(n,G)



