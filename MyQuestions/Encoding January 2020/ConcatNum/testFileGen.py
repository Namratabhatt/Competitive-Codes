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

sys.stdout = open(os.path.join(sys.path[0],"input6.in"),'w+')

digits = ['1','12','134','55','23','100']

number = ""
total = 0
while(total<1000000):

    while(len(number)<10000):
        number+=choice(digits)
    
    
    digits.append(number)
    number+=str(randint(1,9))
    total+=len(number)
    digits.append(number)

digits.pop()
print(len(digits))
print(*digits)