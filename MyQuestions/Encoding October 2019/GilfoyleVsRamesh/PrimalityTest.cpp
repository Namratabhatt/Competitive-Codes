#include<bits/stdc++.h>
using namespace std;

typedef unsigned long long ULL;

ULL mulmod(ULL a, ULL b, ULL c){
    ULL x = 0,y = a%c;
    
    while(b>0){
        if(b&1) x = (x+y)%c;
        y = (y<<1)%c;
        b >>= 1;
    }
    
    return x;
}

ULL pow(ULL a, ULL b, ULL c){
    ULL x = 1, y = a;
    
    while(b>0){
        if(b&1) x = mulmod(x,y,c);
        y = mulmod(y,y,c);
        b >>= 1;
    }
    
    return x;
}

bool miller_rabin(ULL p, int it){
    if(p<2) return false;
    if(p==2) return true;
    if((p&1)==0) return false;
    
    ULL s = p-1;
    while(s%2==0) s >>= 1;
    
    while(it--){
        ULL a = rand()%(p-1)+1,temp = s;
        ULL mod = pow(a,temp,p);
        
        if(mod==-1 || mod==1) continue;
        
        while(temp!=p-1 && mod!=p-1){
            mod = mulmod(mod,mod,p);
            temp <<= 1;
        }
        
        if(mod!=p-1) return false;
    }
    
    return true;
}

int main(){

    //freopen("input0.in","r",stdin);
    // freopen("output0.in","w",stdout);
    int N;
    cin>>N;
    ULL array[N];
    for(int i = 0;i<N;i++){
        cin>>array[i];
    }

    int countleft,countright;
    ULL maxleft,maxright;
    countleft = 0,countright = 0;
    maxleft = -2,maxright = -2;

    for( int i = 0;i<N/2;i++){
        if (miller_rabin(array[i],18) == true){
            if(maxleft ==-2)maxleft=array[i];
            countleft++;
        }
    }
    for(int i = N/2;i<N;i++){
        if (miller_rabin(array[i],18) == true){
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
    //     cout<<miller_rabin(array[i],18)<<" "<<array[i]<<endl;
    // }
    return 0;
}
