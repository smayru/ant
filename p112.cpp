#include <iostream>
using namespace std;

#define MAX_L 10000
int sieve(int n) {
    bool is_prime[MAX_L];
    int prime[MAX_L+1];
    
    int p=0;
    for (int i=0;i<=n;i++){
        is_prime[i]=true;
    }
    for (int i=2;i<=n;i++){
        if (is_prime[i]){
            prime[p++]=i;
            for (int j=2*i;j<=n;j+=i){
                is_prime[j]=false;
            }
        }
    }
    return p;
}
int main(){
    int tmp=sieve(11);
    cout << tmp <<"\n";
    return 0;
}
