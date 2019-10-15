from math import gcd 
from collections import defaultdict, deque
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_input =lambda : map(int, stdin.readline().split())
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

test = int_input()
for i in range(test):
    n = int_input()
    prices = list_input()
    count = 0
    for i in range(n):
        prev_prices = []
        limit = 0
        if i<=5:
            limit = 0
        else:
            limit = i-5
        flag = 0
        for j in range(limit,i):
            if(prices[i]>=prices[j]):
                flag = 1

        if(flag == 0):
            count+=1

    print(count)