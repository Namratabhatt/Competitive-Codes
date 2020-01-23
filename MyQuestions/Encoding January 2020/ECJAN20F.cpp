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


ll tax[MAX],temp[2*MAX],in[2*MAX],out[2*MAX];
int t=0;
vector<int>g[MAX];

ll getSum(ll* BITree, int index) 
{ 
    ll sum = 0;
    index = index + 1; 
    while (index>0) 
    { 
        sum += BITree[index]; 
        index -= index & (-index); 
    } 
    return sum; 
} 
void updateBIT(ll* BITree, int n, int index, ll val) 
{ 
    index = index + 1;
    while (index <= n) 
    {
    BITree[index] += val;
    index += index & (-index); 
    } 
} 
ll *constructBITree(int n) 
{ 
    ll *BITree = new ll[n+1]; 
    for (int i=1; i<=n; i++) 
        BITree[i] = 0; 
    for (int i=0; i<n; i++) 
        updateBIT(BITree, n, i, temp[i]);  
    return BITree; 
}  

void dfs(int u,int parent){
    in[u]=t++;
    for(int child:g[u]){
        if(child!=parent){
            dfs(child,u);
        }
    }
    out[u]=t++;
}

void solve(){
    ll n,Q,i,j,u,x;
    cin>>n>>Q;
    for(i=0;i<n-1;i++){
        cin>>u>>x;
        g[u].push_back(x);
        g[x].push_back(u);
    }
    for(i=1;i<=n;i++)cin>>tax[i];
    tax[1]=0;
    dfs(1,0);

    for(i=1;i<=n;i++){
        temp[in[i]]=tax[i];
        temp[out[i]]=-(tax[i]);
    }

    for(i = 0;i<n*3;i++)
    cout<<temp[i]<<" ";

    ll *BT=constructBITree(t);

    while(Q--){
        cin>>i;
        if(i==1){
            cin>>x;
            cout<<getSum(BT,out[x]-1)<<endl;
        }
        else{
            cin>>x>>u;
            if(x==1)
                continue;
            updateBIT(BT,t,in[x],u);
            updateBIT(BT,t,out[x],-u);
            
        }
    }


}
int main(){
    FAST;
    #ifndef ONLINE_JUDGE
    // freopen("ip6.in","r",stdin);
    // freopen("op6.out","w",stdout);
    #endif
    solve();
}

// 10 10
// 1 2
// 1 3
// 2 4
// 2 5
// 4 7
// 5 8
// 5 9
// 3 6
// 6 10
// 10 5 7 6 8 6 9 5 4 9
// 1 10
// 1 8
// 2 5 9
// 1 9
// 2 2 7
// 1 4
// 1 8
// 2 3 8
// 1 10
// 1 6


// 22
// 18
// 26
// 18
// 34
// 30
// 21