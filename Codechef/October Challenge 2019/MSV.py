from math import gcd 
from math import sqrt
from collections import defaultdict, deque
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_input =lambda : map(int, stdin.readline().split())
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7
factor_dict = {}

# method to print the divisors 
def findDivisors(n) :    
    # List to store half of the divisors 
    for i in range(1, int(sqrt(n) + 1)) : 
          
        if (n % i == 0) :   
            # Check if divisors are equal 
            if (n // i == i) : 
                if i not in factor_dict:
                    factor_dict[i] = 0
                else:
                    factor_dict[i]+=1
            else : 
                # Otherwise print both 
                if i not in factor_dict:
                    factor_dict[i] = 0
                else:
                    factor_dict[i]+=1
                if n//i not in factor_dict:
                    factor_dict[n//i] = 0
                else:
                    factor_dict[n//i]+=1
                  

test = int_input()
for i in range(test):
    n = int_input()
    factor_dict = {}
    result = [0] * n
    sequence = list_input()
    max_val = 0

    for i in range(n):
        findDivisors(sequence[i])
        print(factor_dict)
        if sequence[i] in factor_dict:
            #factor_dict[sequence[i]]+=1
            result[i] = factor_dict[sequence[i]]

    print(result)
    print(max(result))

