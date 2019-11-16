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
    n = int_input()
    a = list_input()
    b = list_input()

    start = False
    prev = -1
    diff = -1
    flag = 0

    for i in range(n):
        if a[i]!=b[i] and a[i] <b[i] and start == False :
            start = True
            diff = b[i] - a[i]
            prev = i
        elif a[i]!=b[i] and ((b[i] -a[i]) == diff) and start == True and prev == i-1:
            prev = i
        elif a[i] == b[i]:
            continue
        else:
            flag = 1

    if flag == 0:
        print("YES")
    else:
        print("NO")