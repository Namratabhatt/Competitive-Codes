import java.util.*;

class Solution{
    
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        
        int test = sc.nextInt();

        while(test-->0){
            int m = sc.nextInt();
            int n = sc.nextInt();
            System.out.println(m%n);
        }

        sc.close();
    }

}