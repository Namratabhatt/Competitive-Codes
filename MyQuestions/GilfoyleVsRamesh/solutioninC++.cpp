#include<bits/stdc++.h>
#include<iostream>
#define ll long long int
using namespace std;


ll exp_pow(ll x, unsigned ll y, ll p) 
{ 
    ll res = 1;      // Initialize result 
  
    x = x % p;  // Update x if it is more than or  
                // equal to p 
  
    while (y > 0) 
    { 
        // If y is odd, multiply x with result 
        if (y & 1) 
            res = (res*x) % p; 
  
        // y must be even now 
        y = y>>1; // y = y/2 
        x = (x*x) % p;   
    } 
    return res; 
} 

bool check_composite(ll n,int a,ll d, ll s){
    ll x = exp_pow(a,d,n);
    if (x ==1 or x == n-1)
    return false;
    for(ll i = 1;i<s;i++){
        x = (x*x)%n;
        if (x == n-1)
        return false;
    }
    return true;
}

int miller_rabin(ll number){
    if (number<2)
    return 0;
    ll r = 0;
    ll d = number-1;
    while((d&1)==0){
        d>>=1;
        r++;
    }
    int base[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    for(int a:base){
        if(number == a)
        return 1;
        if (check_composite(number,a,d,r))
        return 0;
    }
    return 1;
}

int main(){

    // freopen("input0.in","r",stdin);
    // freopen("output0.in","w",stdout);
    int N;
    cin>>N;
    ll array[N];
    for(int i = 0;i<N;i++){
        cin>>array[i];
    }

    int countleft,countright;
    ll maxleft,maxright;
    countleft = 0,countright = 0;
    maxleft = -2,maxright = -2;

    for( int i = 0;i<N/2;i++){
        if (miller_rabin(array[i]) == 1){
            if(maxleft ==-2)maxleft=array[i];
            countleft++;
        }
    }
    for(int i = N/2;i<N;i++){
        if (miller_rabin(array[i]) == 1){
        maxright = array[i];
        countright++;
        }
    }
    //cout<<countleft<<" "<<countright<<" "<<maxleft<<" "<<maxright<<endl;
    if(countleft == countright && maxleft>maxright)
    cout<<"PERFECT"<<endl;
    else
    cout<<"IMPERFECT"<<endl;

    // for(int i = 0;i<N;i++){
    //     cout<<miller_rabin(array[i])<<" "<<array[i]<<endl;
    // }
    return 0;
}

