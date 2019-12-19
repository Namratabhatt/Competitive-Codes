from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

test = int_input()

def isPerm(str1, str2): 
      
    # Get lenghts of both strings 
    n1 = len(str1) 
    n2 = len(str2) 
  
    # If length of both strings is not same, 
    # then they cannot be Permutation 
    if (n1 != n2): 
        return False
  
    # Sort both strings 
    a = sorted(str1) 
    str1 = " ".join(a) 
    b = sorted(str2) 
    str2 = " ".join(b) 
  
    # Compare sorted strings 
    if str1 == str2:
        return True
    else:
        return False

for _ in range(test):
    p = input()
    hash = input()
    flag = 0
    if len(p)>len(hash):
        flag = 0
    else:
        #print(p,hash)
        length = len(p)
        for i in range(0,len(hash)-length+1):
            substring = hash[i:i+length]
            #print(substring)
            if isPerm(substring,p):
                flag = 1
                break
    
    if flag == 1:
        print("YES")
    else:
        print("NO")

#print(isPerm("one","nne"))