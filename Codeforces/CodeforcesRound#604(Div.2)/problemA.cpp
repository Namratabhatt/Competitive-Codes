
#include <bits/stdc++.h>
using namespace std;

char t[]={'a','b','c'};

void solve(){
    int n,i,j;
    string s;
   
    cin>>s;
  
    bool ok=true;
    n=s.length();
    for(i=0;i<(n-1)&&ok;i++){
        if(s[i]=='?'||s[i+1]=='?')
            continue;
        if(s[i]==s[i+1])
            ok=false;
    }
    if(!ok){
        cout<<-1<<endl;
        return;
    }
    
    s=' '+s+' ';
    n+=2;
    int id=0;
    for(i=1;i<n-1;i++){
       
        id=0;
        if(s[i]=='?')
            s[i]=t[id];
        else
            continue;
        if(s[i]==s[i-1])
            s[i]=t[(++id)%3];
        if(s[i]==s[i+1])
            s[i]=t[(++id)%3];
        if(s[i]==s[i-1])
            s[i]=t[(++id)%3];
       
    }
    cout<<s.substr(1,n-2)<<endl;

}
int main(){

    int t;
    cin>>t;
    while(t--)
        solve();
}