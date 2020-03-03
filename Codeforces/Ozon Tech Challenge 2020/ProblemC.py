from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
#from random import randint

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

n,m = multi_int_input()

arr = list_input()

def bruteforce(arr):
    ans = 1
    for i in range(len(arr)):
        num1 = arr[i]
        for j in range(i+1,len(arr)):
            ans*=abs(num1 - arr[j])%m
    return ans



if n<m:
    print(bruteforce(arr))
else:
    print(0)
        
