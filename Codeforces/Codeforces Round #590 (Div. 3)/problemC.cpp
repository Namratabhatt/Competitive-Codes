#include<bits/stdc++.h>
#define FAST ios_base::sync_with_stdio(false);cin.tie(NULL);

using namespace std;
int main()
{
    FAST
	int n;
	int k;
	cin>>n>>k;
	int arr[n];
	queue<int> list;
	bool val=false;
	for(int i=0;i<n;i++)
	{
		cin>>arr[i];
	}
	unordered_map<int, int> m; 
	for(int i=0;i<n;i++)
	{
		int item=arr[i];
        if(m.find(item)==m.end()){
            if(list.size()==k){
                m.erase(list.front());
                list.pop();
            }
            m[item]=1;
            list.push(item);
        }
	}
	cout<<list.size()<<endl;
	 vector<int> t;
    while(!list.empty())
    {
    t.push_back(list.front());
    list.pop();
    }
    for(int i=t.size()-1;i>=0;i--)
        cout<<t[i]<<" ";
	return 0;
}