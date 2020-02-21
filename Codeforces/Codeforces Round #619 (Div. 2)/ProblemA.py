from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
from math import ceil

# int_input=lambda : int(stdin.readline())
# string_input=lambda : stdin.readline()
# multi_int_input =lambda : map(int, stdin.readline().split())
# multi_input = lambda : stdin.readline().split()
# list_input=lambda : list(map(int,stdin.readline().split()))
# string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

test = int(input())

for _ in range(test):
    a = input()
    b = input()
    c = input()

    if b == c:
        print("YES")
    else:
        flag = True
        for i in range(len(a)):
            seti = set([])
            seti.add(a[i])
            seti.add(b[i])
            seti.add(c[i])
            if len(seti) == 2:
                if a[i] == b[i]:
                    flag = False
                    break
            elif len(seti) == 3:
                flag = False
                break
        if flag == False:
            print("NO")
        else:
            print("YES")