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
MOD = pow(10,9)+7


total = 0


import os,sys

sys.stdout = open(os.path.join(sys.path[0],"input3.in"),'w+')

test = 400000
print(test)

product = 1
for _ in range(0,test):

    if _ < 350000:
        numbeingadded = randint(0,5)
        if numbeingadded == 0:
            product = 1
        else:
            product = product*numbeingadded
        if product>10000000:
            numbeingadded = 1
        print(1,numbeingadded)
    else:
        getPro = randint(2,5000)
        print(2,getPro)

