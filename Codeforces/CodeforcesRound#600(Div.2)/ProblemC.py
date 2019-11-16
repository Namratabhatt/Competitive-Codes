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

n,m = multi_int_input()

sweets = list_input()

sorted_sweets = sorted(sweets)

#precomputation
even = 0
odd = 0
summ_array = [0]*n
for i,n in enumerate(sorted_sweets):
    if i>=m:
        summ_array[i] = summ_array[i-m]+sorted_sweets[i]
    else:
        summ_array[i] = sorted_sweets[i]

c= 0
for i in summ_array:
    print(i+c,end = " ")
    c = i+c

