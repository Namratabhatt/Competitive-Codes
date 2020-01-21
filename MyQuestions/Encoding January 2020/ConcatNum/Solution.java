import java.util.Scanner;
import java.util.Arrays;
import java.util.*;
import java.io.*;

class Solution{

    public static void solve(String []input){
        List<String> concatenated = new ArrayList<>();
        Set<String> hashset = new HashSet<>();

        for(String word: input){
            hashset.add(word);
        }

        for(String word:input){
            if(isConcatenated(hashset,word)) 
                concatenated.add(word);
        }

        Collections.sort(concatenated);

        for(int i = 0;i<concatenated.size();i++){
            System.out.print(concatenated.get(i)+" ");
        }
    }

    public static boolean isConcatenated(Set<String> hashset, String word){
        for (int i = 1; i < word.length(); i++) {
            if (hashset.contains(word.substring(0, i))) {
                String rightStr = word.substring(i);
                if (hashset.contains(rightStr) || isConcatenated(hashset, rightStr))
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