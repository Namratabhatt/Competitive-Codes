#include<bits/stdc++.h>
using namespace std;

struct point{
    int id;
    int pos;
};

bool comp(point& a,point& b){
    return a.id<b.id;

}
void solve(){
    int n,i,j;
    cin>>n;
    point arr[n+1];

    for(i=1;i<=n;i++){
        cin>>arr[i].id;
        arr[i].pos=i;
    }
    sort(arr+1,arr+n+1,comp);

    int lmax=0,rmax=0;

    for(i=1;i<=n;i++){
        if(i==1||i==n){
            cout<<1;
            continue;
        }
        lmax=min(lmax,arr[i].pos-arr[1].pos);
        rmax=max(rmax,arr[i].pos-arr[1].pos);
        if(rmax-lmax+1<=i)
            cout<<1;
        else
            cout<<0;

    }
    cout<<endl;
    
}
int main(){
    int t;
    cin>>t;
    while(t--)
        solve();
}