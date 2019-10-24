//PKMKB
#include <bits/stdc++.h>
#define ll  unsigned long long int
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define scanarr(a,b,c) for(int i=b;i<c;i++)cin>>a[i]
#define showarr(a,b,c) for(int i=b;i<c;i++)cout<<a[i]<<" "
#define ln cout<<"\n"
#define FAST ios_base::sync_with_stdio(false);cin.tie(NULL);
#define mod 1000000007
#define MAX 100005
using namespace std;
////////////////////////////////////////////////////////////////CODE STARTS HERE////////////////////////////////////////////////////////////////
void solve(){
    
    string n;
    cin>>n;
 
    if(n.length()==1){
        cout<<n<<endl;
        return;
    }
    if(n.length()==2){
        cout<<to_string((n[0]-'0')^(n[1]-'0'))<<endl;
        return;
    }
    string ans="";
    int l=n.length();
    for(int i=0;i<l;i++)
        ans+=to_string((n[i]-'0')^(n[(i+1)%l]-'0'));
    cout<<ans<<endl;
}  
int main(){
   
    int t;
    cin>>t;
    while(t--)
        solve();        
} 