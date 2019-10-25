from sys import stdin,stdout
from sys import path
import os
import sys

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

# for i in range(5):

#stdin = open(os.path.join(path[0],'input0.in'),'r')

for _ in range(int_input()):
    n=input()
    a=[int(i) for i in n]
    #print("The number is",a)
    ans=''
    for i in range(len(a)-1):
        ans+=str(a[i]^a[i+1])
    if(len(a)>2):
        ans+=str(a[0]^a[-1])
    if(len(a)==1):
        ans=a[0]
    print(ans)
