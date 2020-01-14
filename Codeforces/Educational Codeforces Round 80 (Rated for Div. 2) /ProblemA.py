from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
from math import ceil

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

test = int_input()

for _ in range(test):
    n,d = multi_int_input()

    c = d
    i = 1
    flag = True
    while(c>n):
        c = i+ceil(d/(i+1))
        i+=1
        if(i>n-1):
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
