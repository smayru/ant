
#include <iostream>
using namespace std;
typedef long long ll;

#define MAX_L 10000
#define MAX_SQRT_B 10000
int segment_sieve(ll a,ll b) {
    bool is_prime[MAX_L];
    bool is_prime_small[MAX_SQRT_B];
    for (int i=0;(ll)i*i<b;i++){
        is_prime_small[i]=true;
    }
    for (ll i=0;i<a;i++){
        is_prime[i]=false;
    }
    for (ll i=a;i<b;i++){
        is_prime[i]=true;
    }
    for (int i=2;(ll)i*i<b;i++){
        if (is_prime_small[i]){
            for (int j=2*i;(ll)j*j<b;j+=i) is_prime_small[j]=false;
            for (int j=0;(ll)j<b;j+=i) is_prime[j]=false;
        }
    }
    int sum=0;
    for (ll i=a;i<b;i++) sum+=is_prime[i];
    return sum;
    
}
int main(){
    ll a=22;
    ll b=37;
    int tmp=segment_sieve(a,b);
    cout << tmp <<"\n";
    return 0;
    
}

