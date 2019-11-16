//PKMKB
#include <bits/stdc++.h>
#define ll long long int
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define scanarr(a,b,c) for( i=b;i<c;i++)cin>>a[i]
#define showarr(a,b,c) for( i=b;i<c;i++)cout<<a[i]<<' '
#define ln cout<<'\n'
#define FAST ios_base::sync_with_stdio(false);cin.tie(NULL);
#define mod 1000000007
#define MAX 100005
using namespace std;
////////////////////////////////////////////////////////////////CODE STARTS HERE////////////////////////////////////////////////////////////////

void solve(){

    int n,i;
    
    cin>>n;
    int a[n], b[n];
    scanarr(a,0,n);
    scanarr(b,0,n);

    bool start = false;
    int prev = -1;
    int diff = -1;
    int flag = 0;

    for(i = 0;i<n;i++){
        if (a[i]!=b[i] && a[i] <b[i] && start == false){
            start = true;
            diff = b[i] - a[i];
            prev = i;
        }
        else if( a[i]!=b[i] && ((b[i] -a[i]) == diff) && start == true && prev == i-1)
            prev = i;
        else if (a[i] == b[i])
            continue;
        else
            flag = 1;
    }
    if (flag == 0)
        cout<<("YES")<<endl;
    else
        cout<<("NO")<<endl;   

}
int main(){

    int t;
    cin>>t;
    while(t--)
        solve();
}