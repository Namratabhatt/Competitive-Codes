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

queries = int_input()

for _ in range(queries):
    n = int_input()
    students = list_input()

    dict ={}
    count = 0
    for i in range(0,n):
        for j in range(0,n):
            if i!=j:
                if abs(students[i]-students[j]) == 1:
                    count+=1
    if count >=1:
        print(2)
    else:
        print(1)