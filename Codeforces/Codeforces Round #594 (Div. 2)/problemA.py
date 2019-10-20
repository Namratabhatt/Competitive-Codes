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
    m = int_input()
    m_points  = list_input()
    n = int_input()
    n_points = list_input()

    even = 0
    odd = 0

    for i in (m_points):  
        if i%2 == 0:
            even+=1
        else:
            odd += 1
    final = 0
    for i in n_points:
        if i%2 == 0:
            final+=even
        else:
            final+=odd
    
    print(final)