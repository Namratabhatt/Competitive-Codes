#include<bits/stdc++.h>

using namespace std;

int main(){
    int test,a,b,c;
    cin>>test;
    while(test--){
        cin>>a>>b>>c;
        if (a == 0 || b == 0 || c == 0){
            cout<<"NO"<<endl;
        }
        else{
            if (a*a+b*b == c*c || a*a+c*c == b*b || b*b +c*c == a*a)
                cout<<"YES"<<endl;
            else
                cout<<"NO"<<endl;
        }
    }
    return 0;
}