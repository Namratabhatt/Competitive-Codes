
 
from math import gcd
from math import ceil,floor
from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
import sys



int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7


test = int_input()

for _ in range(test):
    a,b,c,d,k = multi_int_input()
    no_of_pens_req = ceil(a/c)
    no_of_pencils = ceil(b/d)
    if no_of_pens_req+no_of_pencils <= k:
        print(no_of_pens_req,no_of_pencils)
    else:
        print(-1)
    
