import java.util.*;

class ECFBP203{

    static Scanner sc = new Scanner(System.in);
    public static void main(String args[]){
        int test = sc.nextInt();
        while(test-- >0){
            int n = sc.nextInt();
            int arr[] = new int[n];
            int brr[] = new int[n];
            Arrays.fill(brr,0);

            int ptr = 0;
            
            // imput array
            for(int  i = 0;i<n;i++){
                arr[i] = sc.nextInt();
            }

            // operate
            for(int i = 0;i<n;i++){
                if(arr[i]!=0){
                    brr[ptr++] = arr[i];
                }
            }

            for(int i = 0;i<n;i++){
                System.out.print(brr[i]+" ");
            }
            System.out.println();
        }
    }
}