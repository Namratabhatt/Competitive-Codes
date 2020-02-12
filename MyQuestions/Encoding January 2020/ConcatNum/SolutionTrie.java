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
        sc.close();
    }

}

class Trie {
    Trie array[] = new Trie[10];
    boolean isNumber = false;
}