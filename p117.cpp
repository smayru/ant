#include <iostream>
using namespace std;
typedef long long ll;

#define MAX_L 10000
#define MAX_SQRT_B 10000
ll sss(int *v1,int *v2, int n) {
    sort(v1,v1+n);
    sort(v2,v2+n);
    ll ans=0;
    for (int i=0;i<n;i++){
        ans+=(ll) v1[i]*v2[n-i-1];
    }
    return ans;
}
int main(){
    int n=3;
    int v1[]={1,3,-5};
    int v2[]={-2,4,1};
    ll tmp=sss(v1,v2,n);
    cout << tmp <<"\n";
    return 0;
    
}