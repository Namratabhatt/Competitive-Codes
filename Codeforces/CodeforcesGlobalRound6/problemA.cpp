#include<bits/stdc++.h>

using namespace std;

int main(){
    int test;
    cin>>test;
    while(test--){
        
        string number;
        cin>>number;

        vector<int> digitVector;
        int sum = 0;
        int noEven = 0;
        int noZeroes = 0;
        for(char ch: number){
            digitVector.push_back(int(ch) - int('0'));
        }

        for(int i = 0;i<digitVector.size();i++){
            if (digitVector[i]%2 == 0){
                if (digitVector[i] == 0){
                    noZeroes++;
                }
                noEven++;
            }
            sum+=digitVector[i];
        }

        if (sum%3 == 0 && noEven>=2 && noZeroes >=1)
            cout<<"red"<<endl;
        else
            cout<<"cyan"<<endl;
    
    }
}