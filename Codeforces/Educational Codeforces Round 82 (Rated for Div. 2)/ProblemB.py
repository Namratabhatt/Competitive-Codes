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
    
    n,g,b = multi_int_input()

    if g>=n:
        print(n)
    else:
        mini = ceil(n/2)
        no_good = mini//g
        remainder = mini%g
        first_ans = no_good*g +(no_good-1)*b
        if remainder != 0:
            first_ans = (first_ans+b+remainder)
        if first_ans>=n:
            print(first_ans)
        else:
            print(n)