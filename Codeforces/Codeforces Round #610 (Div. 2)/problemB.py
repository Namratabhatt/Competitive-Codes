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
    n,p,k = multi_int_input()

    products = list_input()

    products.sort()

    k_copy = k
    ans1,ans2 = 0,0
    i = 0
    if products[0]>p:
        print(0)
    else:

        cost = products[0]
        start = 2
        items1 = 1
        while(start<n):
            cost+=products[start]
            if cost>p:
                break
            else:
                start+=2
                items1+=2
        items2 = 0
        cost = 0
        start = 1
        while(start<n):
            cost+=products[start]
            if cost>p:
                break
            else:
                start+=2
                items2+=2

        print(max(items1,items2))