import java.util.*;

class ECJAN20F{
    static int MAX = 100005;
    static ArrayList<Integer>[] tree;
    static int[] taxes;
    static int n;
    static int temp[];
    static int t = 0;
    static int in[];
    static int out[];
    static long BIT[];

    public static long getRangeQuery(int pos){
        long sum = 0l;
        pos = pos+=1;
        // System.out.println("Range for "+pos);
        while(pos>0){
            sum+= BIT[pos];
            pos -= (pos & (-pos));
        }
        return sum;
    }

    public static void updateBIT(int pos, int value){
        pos+=1;
        while(pos <= t){
            BIT[pos] += value;
            pos += (pos & (-pos)); 
        }
    }

    public static void constructBIT(){
        BIT = new long[t+1];
        for(int i = 1;i<=t;i++)
            BIT[i] = 0l;
        for(int i = 0;i<t;i++){
            updateBIT(i,temp[i]);
        }
    }

    public static void dfs(int u,int parent){
        in[u] = t++;
        for(int child:tree[u]){
            if(child!=parent)
            dfs(child,u);
        }
        out[u] = t++;
    }

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int queries = sc.nextInt();
        
        tree = new ArrayList[n+1];
        for (int i = 0; i < n+1; i++) { 
            tree[i] = new ArrayList<Integer>(); 
        } 
        temp = new int[2*n];
        in = new int[2*n];
        out = new int[2*n];

        for(int i = 0;i<n-1;i++){
            int u = sc.nextInt();
            int v = sc.nextInt();
            tree[u].add(v);
            tree[v].add(u);
        }

        // System.out.println(tree[6]);
        taxes = new int[n+1];
        for(int i = 1;i<=n;i++)
            taxes[i] = sc.nextInt();
        taxes[1] = 0;
        
        dfs(1,0);

        for(int i = 1;i<=n;i++){
            temp[in[i]] = taxes[i];
            temp[out[i]] = -taxes[i];
        }

        constructBIT();

        while(queries-- > 0){
            int a = sc.nextInt();
            if (a == 1){
                int x = sc.nextInt();
                System.out.println(getRangeQuery(out[x]-1));
            }
            else{
                int x = sc.nextInt();
                int up = sc.nextInt();
                if (x == 1)
                    continue;
                updateBIT(in[x],up);
                updateBIT(out[x],-up);
            }
        }
    }
}