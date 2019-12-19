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
    a,b = multi_int_input()

    diff = abs(a-b)

    if diff == 0:
        print(0)
    else:
        sum = 0
        k = 1
        count = 0
        while not(sum>=diff and (sum-diff)%2 == 0):
            sum+=k
            #print(sum)
            k = k+1
            count+=1
    
        print(count)