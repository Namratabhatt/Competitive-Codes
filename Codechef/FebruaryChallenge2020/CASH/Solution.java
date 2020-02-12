import java.util.*;

class Solution{

    
    public static void printarr(int[] arr, int n){
        for(int i = 0;i<n;i++){
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }

    public static void solve(){
        Scanner sc = new Scanner(System.in);
        int test = sc.nextInt();
        while(test-->0){
            int n = sc.nextInt();
            int k = sc.nextInt();
            int min = Integer.MAX_VALUE;
            int coins[] = new int[n];
            for(int i = 0;i<n;i++){
                coins[i] = sc.nextInt();
            }

            int removeCoin[] = new int[n];
            int addCoin[] = new int[n];

            for(int i = 0;i<n;i++){
                removeCoin[i] = coins[i]%k;
                addCoin[i] = k - coins[i]%k;
            }
            int sum = 0;
            for(int i = 0;i<n;i++){
                sum+=removeCoin[i];
            }
            min = sum;
            if (min<removeCoin[n-1])
            System.out.println(min);
            else{
                min = sum-removeCoin[n-1];
                
            }
        }
        sc.close();
    }

    public static void main(String args[]){
        solve();
    }

}