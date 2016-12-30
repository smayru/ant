#p34
import numpy as np

n=4
a=[1,2,4,7]
k=13

def dfs(i,sum_val):
	if i==n:
		return sum_val==k
	elif dfs(i+1,sum_val):
		return True
	elif dfs(i+1,sum_val+a[i]):
		return True
	return False
def test(n,m,k):
	if dfs(0,0)==True:
		print('yes')
	else:
		print('no')
if __name__ == '__main__':
	test(n,a,k)

