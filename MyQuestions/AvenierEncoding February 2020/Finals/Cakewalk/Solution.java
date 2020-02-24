import java.util.*;

class Solution{
    
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        
        int test = sc.nextInt();
        System.out.println(test);
        while(test-->0){
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            
            if (a == 0 || b == 0 || c == 0){
                System.out.println("NO");
            }
            else{
                if (((a*a + b*b) == c*c) || ((b*b + c*c) == a*a) || ((a*a + c*c) == b*b))
                    System.out.println("YES");
                else
                    System.out.println("NO");
        }

        sc.close();
        }

    }
}

