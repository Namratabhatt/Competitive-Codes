import java.util.*;

class Solution{

    public static void solve(int []a, int []b, int n){

        Arrays.sort(a);
        Arrays.sort(b);
        long result = 0l;
        for(int i = 0;i<n;i++){
            result += Math.min(a[i],b[i]);
        }
        System.out.println(result);
    }

    public static void main(String args[]){
        Scanner sc  = new Scanner(System.in);
        int test = 0;
        test = sc.nextInt();
        while(test-- >0){
            
            int n = sc.nextInt();
            int [] a = new int[n];
            int [] b = new int[n];

            for(int i = 0;i<n;i++){
                a[i] = sc.nextInt();
            }

            for(int i = 0;i<n;i++){
                b[i] = sc.nextInt();
            }

            solve(a,b,n);

        }

        sc.close();
    }
}