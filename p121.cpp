#include <iostream>
#include <utility>      // std::swap
using namespace std;
typedef long long ll;

#define MAX_Q 100

int main() {
    int P=20;
    int Q=3;
    int A[MAX_Q+2];
    int dp[MAX_Q+1][MAX_Q+2];
    A[0]=0;
    A[1]=3;
    A[2]=6;
    A[3]=14;
    A[Q+1]=P+1;
    for (int q=0;q<=Q;q++){
        dp[q][q+1]=0;
    }
    for (int w=2;w<=Q+1;w++){
        for (int i=0;i+w<=Q+1;i++){
            int j=i+w,t=INT_MAX;
            for (int k=i+1;k<j;k++){
                t=min(t,dp[i][k]+dp[k][j]);
            }
            dp[i][j]=t+A[j]-A[i]-2;
        }
    }
//    int tmp=solve(N,M);
    cout << dp[0][Q+1] <<"\n";
    return 0;
}
