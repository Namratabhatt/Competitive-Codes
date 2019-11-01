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

def hcfnaive(a,b): 
    if(b==0): 
        return a 
    else: 
        return hcfnaive(b,a%b)

test = int_input()

for _ in range(test):
    a,b = multi_int_input()
    gcd = hcfnaive(a,b)
    if a==1 or b==1 or gcd==1:
        print("Finite")
    else:
        print("Infinite")