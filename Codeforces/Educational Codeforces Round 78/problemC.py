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

for _ in range(test):
    n = int_input()
    jars = list_input()

    Type = {1:1,2:-1}
    dicti = {}
    
    DIFF = 0   
    dicti[0] = 0 
    for i,ch in enumerate(jars[:n]):
        DIFF += Type[ch]
        dicti[DIFF] = i+1

    ans = 0
    jars.reverse()
    
    if 0 in dicti:
        ans = dicti[0]

    DIFF = 0
    
    for i,ch in enumerate(jars[:n]):
        DIFF+=Type[ch]
        if -DIFF in dicti:
            ans = max(ans, dicti[-DIFF] + i +1)
    print(2*n -ans)