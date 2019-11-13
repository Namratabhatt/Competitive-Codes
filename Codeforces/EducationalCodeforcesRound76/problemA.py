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

test = int_input()

for _ in range(test):
    n,x,a,b = multi_int_input()
    if b<a:
        a,b = b,a

    if x == 0:
        print(b-a)
    else:
        
        while(x>0 and b<n):
            b = b+1
            x = x-1
        while(x>0 and a>1):
            a = a-1
            x = x-1

        print(b-a)