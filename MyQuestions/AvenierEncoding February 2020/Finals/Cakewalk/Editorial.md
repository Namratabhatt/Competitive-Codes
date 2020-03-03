
[Practice](https://www.codechef.com/ENFE2020/problems/ECFEB201)
[Encoding February 2020 Finals Contest](https://www.codechef.com/ENFE2020?itm_campaign=contest_listing)

***Author:***  [arnie8991](https://www.codechef.com/users/arnie8991)
***Tester:***  [nutella](https://www.codechef.com/users/nuttela)
***Editorialist:***  [arnie8991](https://www.codechef.com/users/arnie8991)

# DIFFICULTY:
Cake Walk

# PREREQUISITES:
Logical Reasoning, Maths, Pythagoras Theorem
 
# EXPLANATION:

According to the problem 3 lengths will be given and we have been asked to determine if the three lengths form a Triangle or not. The way we figure this out is to check at first if any of the three lengths contain 0. If there is a length that is 0, we can say for sure that a triangle cannot be built with the length. After this checking, we apply pythagoras theorem on the three lengths and check if they the sum of the square of any two sides is equal to the third side or not. If yes, we can safely say that the three sides can form a triangle. 

# SOLUTIONS:

[details="Setter's Solution"]

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


[details="Tester's Solution"]
