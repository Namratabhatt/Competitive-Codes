from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint,randrange,choice

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())

test = int_input()

for _ in range(test):
    n = int_input()
    arr = list_input()
    brr = [0 for i in range(n)]

    ptr = 0
    for i in range(n):
        if arr[i]!=0:
            brr[ptr] = arr[i];
            ptr+=1

    print(*brr)
