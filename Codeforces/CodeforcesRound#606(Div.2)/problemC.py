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

test= int_input()

for _ in range(test):
    n = string_input()
    result = set([])
    c = 0
    for i in range(len(n)):
        if i+2<len(n):
            if n[i]+n[i+1]+n[i+2] ==  "two":
                if i+4 <len(n):
                    if n[i+3] == "n" and n[i+4] == "e":
                        result.add(i+2)
                        c+=1
                    else:
                        result.add(i+1)    
                        c+=1
                else:
                    result.add(i+1)
                    c+=1
            if n[i]+n[i+1]+n[i+2] ==  "one":
                if i not in result:
                    result.add(i+1)
                    c+=1

    print(c)
    for elements in result:
        print(elements+1,end = " ")
    print()