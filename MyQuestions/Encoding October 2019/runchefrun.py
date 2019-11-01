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

for i in range(test):
    N,K = multi_int_input()

    sum = 0

    multiple = K
    if K>N:
        print(N%MOD)
    else:
        while(multiple<=N):
            sum+=(multiple*2)
            multiple+=K
            
        sum+=N
        print(sum%MOD)