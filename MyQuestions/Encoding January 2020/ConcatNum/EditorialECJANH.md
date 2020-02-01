# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ECJAN20H)
[Encoding October 2019 Contest](https://www.codechef.com/ENJA2020?itm_campaign=contest_listing)

***Author:***  [arnie8991](https://www.codechef.com/users/arnie8991)
***Tester:***  [nutella](https://www.codechef.com/users/nuttela)
***Editorialist:***  [arnie8991](https://www.codechef.com/users/arnie8991)

# DIFFICULTY:
MEDIUM-HARD

# PREREQUISITES:
Tries
 
# EXPLANATION:

This problem is exactly similar to [ECJAN20G](https://www.codechef.com/problems/ECJAN20G) just the difference being that the numbers are in range 1e+10000. In order to handle such big numbers if the DP/DFS approach is used on this it will result in TLE as finding substring will be essentially an O(n). The correct way to do this is by using a Tries DS. Each number is added as a string to the trie and for each character(each digit of the original number) we check if that substring is present in the Trie or not. Using this method we dont have to find substrings and thus execution time is faster.

# SOLUTIONS:

[details="Setter's Solution"]

    import java.util.Scanner;
    import java.util.Arrays;
    import java.util.*;
    import java.io.*;

    class Main{

        public static void solve(String[] numbers) {
            Trie root = new Trie();
            for(int i = 0; i < numbers.length; i++) {
                if( numbers[i].length() > 0 )
                    buildTrie(root, numbers[i]);
            }
        
            List<String> resultList = new ArrayList<String>();
            for(int i = 0; i < numbers.length; i++)
                if( search(root, numbers[i], 0, 0) )
                    resultList.add(numbers[i]);

            System.out.println(resultList.size());
        }
        
        public static void buildTrie(Trie root, String number) {
            Trie current = root;
            for(int i = 0; i < number.length(); i++) {
                int index = number.charAt(i) - '0';
                if( current.array[index] == null )
                    current.array[index] = new Trie();
                current = current.array[index];
            }
            current.isNumber = true;
        }
        
        public static boolean search(Trie root, String number, int begin, int num) {
            Trie current = root;
            for(int i = begin; i < number.length(); i++) {
                int index = number.charAt(i) - '0';
                if( current.array[index] == null )
                    return false;
                current = current.array[index];
                if( current.isNumber && search(root, number, i + 1, num + 1) ) 
                    return true;
            }
            return num >= 1 && current.isNumber;
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

    class Trie {
        Trie array[] = new Trie[10];
        boolean isNumber = false;
    }

[details="Tester's Solution"]