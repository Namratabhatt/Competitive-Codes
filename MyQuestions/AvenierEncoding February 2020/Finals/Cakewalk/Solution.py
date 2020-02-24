# Given 3 lengths of a triangle, print if its a right angled triangle

from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
# from random import randint,randrange,choice
import heapq

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())

import os,sys

stdin = open(os.path.join(sys.path[0],'input0.in'),'r')
sys.stdout = open(os.path.join(sys.path[0],'output0.in'),'w')

test = int_input()

for _ in range(test):
    a,b,c = multi_int_input()
    if a==0 or b == 0 or c  == 0:
        print("NO")
    else:
        if (a**2 + b**2 == c**2) or (a**2 +c**2 == b**2) or (b**2 + c**2 == a**2):
            print("YES")
        else:
            print("NO")