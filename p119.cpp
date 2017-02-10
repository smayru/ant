#include <iostream>
#include <utility>      // std::swap
using namespace std;
typedef long long ll;

#define MAX_N 100

int solve(const int N,int M[MAX_N][MAX_N]){
    int a[N];
    int res=0;
    for (int i=0;i<N;i++){
        a[i]=-1;
        for (int j=0; j<N; j++){
            if (M[i][j]==1)a[i]=j;
        }
    }
    
    for (int i=0; i<N;i++){
        int pos=-1;
        for (int j=i;j<N;j++){
            if (a[j]<=i){
                pos=j;
                break;
            }
        }
        for (int j=pos;j>i;j--){
            std::swap(a[j],a[j-1]);
            res++;
        }
    }
    return res;
}
int main() {
    const int N=3;
    int M[MAX_N][MAX_N];
    M[0][0]=0;
    M[0][1]=0;
    M[0][2]=1;
    M[1][0]=1;
    M[1][1]=0;
    M[1][2]=0;
    M[2][0]=0;
    M[2][1]=1;
    M[2][2]=0;
    int tmp=solve(N,M);
    cout << tmp <<"\n";
    return 0;
}
