#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n,i,j,temp;
    cin>>n;
    int a,b,c;
    bool ok =true;
    for(i=2;i<=sqrt(n);i++){
        if(n%i==0){
            a=i;
            temp=n/i;
            for(j=i+1;j<=sqrt(temp);j++){
                if(temp%j==0&&(temp/j!=a&&temp/j!=j)){
                    cout<<"YES"<<endl;
                    cout<<a<<" "<<j<<" "<<temp/j<<endl;
            
                    return;
                }
            }
        }
    }
    cout<<"NO"<<endl;
}
int main(){

    int t;
    cin>>t;
    while(t--)
        solve();
}