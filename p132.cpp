#include <iostream>
#include <utility>      // std::swap
#include <math.h>
using namespace std;
typedef long long ll;

#define MAX_N 10000
#define INF 10000

bool C(double x,double *w, double *v,int n,int k){
    double y[n];
    for (int i=0;i<n;i++){
        y[i]=v[i]-x*w[i];
    }
    sort(y,y+n);
    double sum=0;
    for (int i=0; i<k;i++){
        sum+=y[n-i-1];
    }
    return sum>=0;
}



int main() {
    int n=3;
    int k=2;
    double w[n];
    w[0]=2;
    w[1]=5;
    w[2]=2;
    double v[n];
    v[0]=2;
    v[1]=3;
    v[2]=1;
    
    double lb=0,ub=INF;
    for (int i=0;i<100;i++){
        double mid=(lb+ub)/2;
        if (C(mid,w,v,n,k)) lb=mid;
        else ub=mid;
    }
    
    

    cout << ub<<"\n";
    return 0;
}
