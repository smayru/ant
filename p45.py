#p45

import numpy as np

N=6
s='ACDBCB'

def test(N,s):
	t=''

	for i in range(N):
		tmp1=s
		tmp2=s[::-1]
		if tmp1<tmp2:
			t+=tmp1[0]
			s=s[1::]
		else:
			t+=tmp2[0]
			s=s[0:len(s)-1]
	print(t)

if __name__ == '__main__':
	test(N,s)
