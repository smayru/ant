#include <iostream>
#include <utility>      // std::swap
#include <math.h>
using namespace std;
typedef long long ll;

#define MAX_Q 100

bool C(double x,int N,double *L, int K){
    int num=0;
    for(int i=0;i<N;i++){
        num+=(int)(L[i]/x);
    }
    return num>=K;
}

int main() {
    int N=4;
    int K=11;
    double L[N];
    L[0]=8.02;
    L[1]=7.43;
    L[2]=4.57;
    L[3]=5.39;
    
    double lb=0, ub=INT_MAX;
    for (int i=0;i<100;i++){
        double mid =(lb+ub)/2;
        if (C(mid,N,L,K))lb=mid;
        else ub=mid;
    }
    
    cout << floor(ub*100)/100<<"\n";
    return 0;
}
