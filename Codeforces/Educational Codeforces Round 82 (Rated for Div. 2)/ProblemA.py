from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
from math import ceil

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

test = int_input()

for _ in range(test):

    string = string_input()

    countOne = 0
    start = False
    counter = 0
    temp = 0

    for i in string:
        if i == '1':
            countOne+=1
        if i == '1' and start == False:
            start = True
        elif i=='0' and start == True:
            temp+=1
        elif i == '1' and start == True:
            counter+=temp
            temp = 0

    #print(countOne)
    if countOne == 0:
        print(0)
    else:
        print(counter)
    
