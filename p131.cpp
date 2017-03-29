#include <iostream>
#include <utility>      // std::swap
#include <math.h>
using namespace std;
typedef long long ll;

#define MAX_Q 100
#define INF 10000

bool C(int d,double *X,int N,int M){
    int last=0;
    for (int i=1;i<M;i++){
        int crt=last+1;
        while(crt<N && X[crt]-X[last]<d){
            crt++;
        }
        if (crt==N) return false;
        last=crt;
    }
    return true;
}

int main() {
    int N=5;
    int M=3;
    double X[N];
    X[0]=1;
    X[1]=2;
    X[2]=8;
    X[3]=4;
    X[4]=9;
    sort(X,X+N);
    double lb=0, ub=INT_MAX;
    while (ub-lb>1){
        int mid=(lb+ub)/2;
        if(C(mid,X,N,M)){
            lb=mid;
        }
        else ub=mid;
    }
    
    
    
    cout << lb<<"\n";
    return 0;
}
