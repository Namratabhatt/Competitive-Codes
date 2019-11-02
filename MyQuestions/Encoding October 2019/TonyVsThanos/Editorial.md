# PROBLEM LINK:

[Practice](https://www.codechef.com/ENOC2019/problems/TVT)
[Encoding October 2019 Contest](https://www.codechef.com/ENOC2019?order=desc&sortBy=successful_submissions)

***Author:***  [arnie8991](https://www.codechef.com/users/arnie8991)
***Tester:***  [horsbug98](https://www.codechef.com/users/horsbug98)
***Editorialist:***  [arnie8991](https://www.codechef.com/users/arnie8991)

# DIFFICULTY:
EASY

# PREREQUISITES:
[Dequeue](https://en.wikipedia.org/wiki/Double-ended_queue)
 
# EXPLANATION:

The trick to solving this within the given constraints is to use a dequeue and keep track of the elements inside the array/list using a dictionary/map.
Take a dequeue Li and each time Tony tries to enter a number check if we can enter the number or not and then do a push_right and in order to remove one of his element do a remove_front.  Do a push_left and remove_back in case of Thanos.
In order to see if an element can be entered in Li or not check:
1. If its aldready there in Li
2. If the list is full, 
    * Check if the other person has got some elements to remove. 
    * If the other person has no elements to remove we cannot enter the element. 

# SOLUTIONS:

[details="Setter's Solution"]
    from collections import deque

    test  = int(input())

    for _ in range(test): 
        tony = []
        thanos = []
        n,k = map(int,input().split())
        #print(n,k)
        tony = [int(x) for x in input().split()]
        thanos = [int(x) for x in input().split()]

        list_numbers = []
        li = deque(list_numbers)

        present_elements = {}

        no_tony = 0 
        no_thanos = 0
        
        for i in range(0,n):
            #Tony's turn 
            if (tony[i] not in present_elements or present_elements[tony[i]] == 0):
                if len(li) == k and no_thanos>0:
                    x = li.popleft()
                    present_elements[x] = 0
                    no_thanos-=1
                if(len(li)<k):
                    li.append(tony[i])
                    no_tony+=1
                    present_elements[tony[i]] = 1
                
            #Thanos's turn
            if (thanos[i] not in present_elements or present_elements[thanos[i]] == 0):
                if len(li) == k and no_tony>0:
                    x = li.pop()
                    present_elements[x] = 0
                    no_tony-=1
                if(len(li)<k):
                    li.appendleft(thanos[i])
                    no_thanos+=1
                    present_elements[thanos[i]] = 1
                
            # print(li)
            # print(present_elements)
            # print(count_list)

        if no_tony>no_thanos:
            print('TONY')
        elif no_tony<no_thanos:
            print('THANOS')
        else:
            print('RUN TONY')
[/details]

[details="Tester's Solution"]
    #include "bits/stdc++.h"
    using namespace std;
    
    #define ll long long
    #define ull unsigned long long
    #define ld long double
    #define pb push_back
    #define ppb pop_back
    #define pii pair<ll, ll>
    #define vi vector<ll>
    #define vull vector<ull>
    #define vpii vector<pii>
    #define mt make_tuple
    #define ff first
    #define ss second
    #define uset unordered_set
    #define umap unordered_map
    #define all(x) x.begin(), x.end()
    #define revall(x) x.rbegin(), x.rend()
    #define rep(i, j, k) for(ll i = j; i < (k); ++i)
    #define repr(i, j, k) for(ll i = k-1; i >= (j); --i)
    #define fastio ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    #define T int tt; cin>>tt; while(tt--)
    
    const ll MOD = (ll)(1e9+7);
    const int inf = (int)INFINITY;
    const ll INF = (ll)INFINITY;
    const int MAX = (int)(1e6+5);
    
    vi primes;
    ll nI[MAX],fI[MAX],fact[MAX];
    
    ll max(ll a,ll b){return a>b?a:b;}
    ll min(ll a,ll b){return a<b?a:b;}
    ll gcd(ll a,ll b){while(b){ll t=a;a=b;b=t%b;}return a;}     
    ll lcm(ll a,ll b){return (max(a,b)/gcd(a,b))*min(a,b);}
    bool isPrime(ll n){if(n<=1)return 0;if(n<=3)return 1;if(n%2==0||n%3==0)return 0;for(ll i=5;i*i<=n;i+=6)if(n%i==0||n%(i+2)==0)return 0;return 1;}
    void find_primes(ll n = 100000000){ll limit=floor(sqrt(n))+1;vi test;test.pb(2),primes.pb(2);for(ll i=3;i<limit;i+=2)if(isPrime(i))test.pb(i),primes.pb(i);ll lo=limit,hi=2*limit;bool p[limit];while(lo<n){if(hi>n)hi=n;
    memset(p,true,sizeof(p)); for(int i=0;i<test.size();++i){ll mn=(lo/test[i])*test[i];if(mn<lo)mn+=test[i];for(ll j=mn;j<hi;j+=test[i])p[j-lo]=0;}rep(i,0,limit)if(p[i] && i+lo<hi)primes.pb(i+lo); lo+=limit,hi+=limit;}}
    ll modmult(ll a,ll b){ll res=0;a%=MOD;while(b){if(b&1)res=(res+a)%MOD;a=(a<<1)%MOD;b>>=1;}return res;}
    ll modexpo(ll a,ll b){ll res=1;a%=MOD;while(b){if(b&1)res=(res*a)%MOD;a=(a*a)%MOD;b>>=1;}return res;}
    ll nCr(ll n,ll r){ll res=1;if(r>n>>1)r=n-r;rep(i,0,r){res=(res*(n-i))%MOD;res=(res*modexpo(i+1,MOD-2))%MOD;}return res;}
    void binomial_pre(){nI[0]=nI[1]=fI[0]=fI[1]=fact[0]=1;rep(i,2,MAX)nI[i]=nI[MOD%i]*(MOD-MOD/i)%MOD;rep(i,2,MAX)fI[i]=(nI[i]*fI[i-1])%MOD;rep(i,1,MAX)fact[i]=(fact[i-1]*i)%MOD;}
    ll binomial(ll n,ll r){if(n<r)return 0;return ((fact[n]*fI[r])%MOD*fI[n-r])%MOD;}
    
    int main() {
        fastio;
        //find_primes();
        //binomial_pre();
        #define JUDGE
        #ifndef JUDGE
            freopen("input4.in", "r", stdin);
            freopen("output4.out", "w", stdout);
            freopen("error.txt", "w", stderr);
        #endif
        ll x = 1e5, xx = 1e9;
        int t;
        cin >> t;
        assert(t >= 1 && t <= 100);
        while(t--) {
            ll n, k, tonyc = 0, thanosc = 0;
            cin >> n >> k;
            assert(n >= 1 && n <= x);
            assert(k >= 1 && k < 2*n);
            vi a(n), b(n);
            rep(i, 0, n) {
                cin >> a[i];
                assert(a[i] >= 1 && a[i] <= xx);
            }
            rep(i, 0, n) {
                cin >> b[i];
                assert(b[i] >= 1 && b[i] <= xx);
            }
            vi tony, thanos;
            set<int> s;
            rep(i, 0, n) {
                if(!s.count(a[i])) {
                    if(s.size() == k && thanosc) {
                        s.erase(thanos.back());
                        thanos.ppb();
                        --thanosc;
                    }
                    if(s.size() < k) {
                        s.insert(a[i]);
                        tony.pb(a[i]);
                        ++tonyc;
                    }
                }
                if(!s.count(b[i])) {
                    if(s.size() == k && tonyc) {
                        s.erase(tony.back());
                        tony.ppb();
                        --tonyc;
                    }
                    if(s.size() < k) {
                        s.insert(b[i]);
                        thanos.pb(b[i]);
                        ++thanosc;
                    }
                }
            }
            if(tonyc > thanosc)
                cout << "TONY";
            else if(thanosc > tonyc)
                cout << "THANOS";
            else
                cout << "RUN TONY";
            cout << '\n';
        }
        return 0;
    }
[/details]