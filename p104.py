#p104
import numpy as np

N=4
ML=2
MD=1
AL=[1,2]
BL=[3,4]
DL=[10,20]
AD=[2]
BD=[3]
DD=[3]




def update(x,y):
	if x>y:
		x=y
		updated=True
	else:
		updated=False
	return [x,updated]

def bellmanford(d):
	for k in range(N):
		updated=False
		for i in range(N-1):
			if d[i+1]<inf :
				[d[i],tmp]=update(d[i],d[i+1])
				updated+=tmp
		for i in range(ML):
			if d[AL[i]-1]<inf :
				[d[BL[i]-1],tmp]=update(d[BL[i]-1],d[AL[i]-1]+DL[i])
				updated+=tmp
		for i in range(MD):
			if d[BD[i]-1]<inf :
				[d[AD[i]-1],tmp]=update(d[AD[i]-1],d[BD[i]-1]-DD[i])
				updated+=tmp
	return d
def test(N,ML,MD,AL,BL,DL,AD,BD,DD):
    inf=100000
    d=np.zeros([N])+inf
    updated=False#各ループで更新が行われたか
    d[0]=0
    d=bellmanford(d)
    print(d[N-1])
if __name__ == '__main__':
    test(N,ML,MD,AL,BL,DL,AD,BD,DD)
