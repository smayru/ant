#include <iostream>
using namespace std;
typedef long long ll;

#define MAX_L 10000
#define MAX_SQRT_B 10000
ll mod_pow(ll x,ll n,ll mod) {
    ll res=1;
    while (n>0){
        if (n&1) res=res*x %mod;
        x=x*x%mod;
        n>>=1;
    }
    return res;
    
}
int main(){
    ll x=4;
    ll n=17;
    ll mod=17;
    ll tmp=mod_pow(x,n,mod);
    cout << tmp <<"\n";
    return 0;
    
}