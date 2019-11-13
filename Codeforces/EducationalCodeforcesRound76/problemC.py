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
    n = int_input()
    array = list_input()

    dictionary = {}

    for i,n in enumerate(array):
        if n in dictionary:
            dictionary[n].append(i)
        else:
            dictionary[n] = [i]
    mini = 9999999999999999
    for elements in dictionary:
        if len(dictionary[elements]) >0:
            for i in range(1,len(dictionary[elements])):
                mini = min(mini,dictionary[elements][i] - dictionary[elements][i-1])

    if mini == 9999999999999999:
        print(-1)
    else:
        print(mini+1)