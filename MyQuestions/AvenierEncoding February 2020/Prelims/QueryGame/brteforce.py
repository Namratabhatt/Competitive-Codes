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

# import os,sys

# stdin = open(os.path.join(sys.path[0],"input4.in"),'r')
# sys.stdout = open(os.path.join(sys.path[0],"output4.in"),'w+')

queries = int_input()

cumlist = []
previous = 1

def add(n):
    global previous
    global cumlist
    cumlist.append(n)

def getPro(n):
    global cumlist
    prod = 1
    for i in range(1,n+1):
        prod = prod*cumlist[-1*i]
    print(prod)

for _ in range(queries):
    typeQuery,n = multi_int_input()
    if typeQuery == 1:
        add(n)
    elif typeQuery == 2:
        getPro(n)