#p107

import numpy as np

P1=[1,11]
P2=[5,3]

def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)
def test(P1,P2):
	a=np.abs(P1[0]-P2[0])
	b=np.abs(P1[1]-P2[1])



	tmp=gcd(a,b)
	ans=max(a/tmp,b/tmp)+1
	print(ans)
if __name__ == '__main__':
	test(P1,P2)