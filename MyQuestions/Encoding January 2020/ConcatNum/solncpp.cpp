/* nuttela - Soham Chakrabarti */
 
#include <bits/stdc++.h>
 
using namespace std;
 
#define IO ios_base::sync_with_stdio(false);cin.tie(NULL);
#define ff first
#define ss second
 
typedef long long ll;
typedef long double ld;
typedef pair <int, int> pii;
 
const int N = 1e6+6;
const int inf = INT_MAX;
const ll MOD = 1e9 + 7;
 
/*typedef struct data
{
  data* bit[2];
  int val = 0;
} trie;
 
void insert(int x){
 
  trie* curr = head;
  for (int i = 30; i >= 0; --i)
  {
    int b = x&(1<<i);
    if(!curr->bit[b]){
      curr->bit[b] = new trie();
    }
    curr = curr->bit[b];
  }
  curr->val=x;
}
 
int minXor(int x){
  trie* curr = head;
 
}*/
 
unordered_map<string,bool> present;
 
bool go(string a){
  //cout << a << endl;
  int n=a.length();
  for (int i = 1; i < n; ++i)
  {
    if(present[a.substr(0,i)]){
      if(present[a.substr(i,n)]||go(a.substr(i,n)))return true;
    }
  }return false;
}
int main() {
  IO;
  //int t;cin>>t;
  //while(t--){
  int n;cin>>n;
  string arr[n];
  ll ans=0;
  for (int i = 0; i < n; ++i)
    cin>>arr[i], present[arr[i]]=1;
  for (int i = 0; i < n; ++i)
  {
   if(go(arr[i]))++ans;
  }
  cout<<ans;
  //}
 
  return 0;
}