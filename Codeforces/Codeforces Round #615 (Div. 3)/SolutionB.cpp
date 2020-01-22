//PKMKB
#include <bits/stdc++.h>

#define FAST ios_base::sync_with_stdio(false);cin.tie(NULL);
#define mod 1000000007
#define MAX 100005
using namespace std;
////////////////////////////////////////////////////////////////CODE STARTS HERE////////////////////////////////////////////////////////////////
struct point{
    int x;
    int y;
};
bool cmp(point& a,point& b){
    if(a.y==b.y)
        return a.x<b.x;
    return a.y<b.y;
}
void solve(){
    
    int n,i,j,x,y;
    cin>>n;
    point arr[n+1];
    arr[0].x=arr[0].y=0;
    for(i=1;i<=n;i++){
        cin>>arr[i].x;
        cin>>arr[i].y;
    }
    sort(arr+1,arr+n+1,cmp);
    bool ok=true;

    for(i=1;i<=n;i++){
        if((arr[i].x<arr[i-1].x)||(arr[i].y<arr[i-1].y)){
            ok=false;
            break;
        }
    }
    if(!ok){
        cout<<"NO"<<endl;
        return;
    }
    cout<<"YES"<<endl;
    string ans="";
    for(i=1;i<=n;i++){
        for(j=0;j<(arr[i].x-arr[i-1].x);j++)
            ans+="R";
        for(j=0;j<(arr[i].y-arr[i-1].y);j++)
            ans+="U";
    }
    cout<<ans<<endl;

}
int main(){

    int t;
    cin>>t;
    while(t--)
        solve();
}