from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7


test = int_input()

for i in range(test):
    n = string_input()
    sum = 0
    twos = 0
    zeroes = 0
    for ch in n:
        if ch != '\n':
            sum+=int(ch)
            if int(ch)%2 == 0:
                if ch == '0':
                    zeroes+=1   
                twos+= 1
    #print(twos,zeroes)
    if (sum %3 == 0 and twos>1 and zeroes>=1):
        print('red')
    else:
        print('cyan')