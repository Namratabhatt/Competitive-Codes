#include <bits/stdc++.h>
#define ll long long int

#define FAST ios_base::sync_with_stdio(false);cin.tie(NULL);
#define mod 1000000007
using namespace std;

void dfs(vector<int> *graph,ll *bacterias,int u,int parent){
    
    for(int child:graph[u]){
        if(child==parent)
            continue;
            
        dfs(graph,bacterias,child,u);
    }
    if(graph[u].size()>1||(u==1&&graph[u].size()>0))
        bacterias[u]=0;

    bacterias[u]+=bacterias[parent];
}

int main() {
    FAST

    int N,Queries,i,x,y;

    char character;

    cin>>N>>Queries;
    vector<int>graph[N+1];
    ll bacterias[N+1];

    bacterias[0]=0;

    for(i=1;i<N;i++){
        cin>>x>>y;
        graph[x].push_back(y);
        graph[y].push_back(x);
    }
    for(i=1;i<=N;i++)
    cin>>bacterias[i];

    while(Queries--){
        cin>>character;

        if(character=='?'){
            cin>>x;
            dfs(graph,bacterias,1,0);

            cout<<bacterias[x]<<endl;
        }
        else{
            cin>>x>>y;
            dfs(graph,bacterias,1,0);

            bacterias[x]+=y;            
        }
    }   
}