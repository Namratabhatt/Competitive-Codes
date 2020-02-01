# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ECJAN20G)
[Encoding October 2019 Contest](https://www.codechef.com/ENJA2020?itm_campaign=contest_listing)

***Author:***  [arnie8991](https://www.codechef.com/users/arnie8991)
***Tester:***  [nutella](https://www.codechef.com/users/nuttela)
***Editorialist:***  [arnie8991](https://www.codechef.com/users/arnie8991)

# DIFFICULTY:
MEDIUM

# PREREQUISITES:
Strings, DP/DFS
 
# EXPLANATION:

The quickest and simplest way to solve this problem is by using the DFS with memoization. Store all the numbers in the input array as strings in a hashset or a map and then for every string check if the substring of this string is present in the hashset or map. Lets say we have a string A of length say n, and we have a function 'isValidSubstring' that takes a string as an argument and checks if that substring is present in the hashset or map. The DP equation will be the following.

return True if A[0:a] in hashset || isValidSubstring[a:]

NOTE: This problem can also be implemented with Tries ds.

# SOLUTIONS:

[details="Setter's Solution"]

    import java.util.Scanner;
    import java.util.Arrays;
    import java.util.*;
    import java.io.*;

    class Main{

        public static void solve(String []input){
            List<String> concatenated = new ArrayList<>();
            Set<String> hashset = new HashSet<>();

            for(String word: input){
                hashset.add(word);
            }

            for(String word:input){
                if(isValidSubstring(hashset,word)) 
                    concatenated.add(word);
            }

            System.out.println(concatenated.size());
        }

        public static boolean isValidSubstring(Set<String> hashset, String word){
            for (int i = 1; i < word.length(); i++) {
                if (hashset.contains(word.substring(0, i))) {
                    String rightStr = word.substring(i);
                    if (hashset.contains(rightStr) || isValidSubstring(hashset, rightStr))
                        return true;
                }
            }
            return false;
        }

        public static void main(String args[]){
            Scanner sc = new Scanner(System.in);
            int n;
            String input[];
            
            n = sc.nextInt();
            input = new String[n];
            for(int i = 0;i<n;i++){
                input[i] = sc.next();
            }
            solve(input);
        }

    }

[details="Tester's Solution"]