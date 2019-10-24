from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
#from random import randint
MOD = pow(10,9)+7

# stdin = open('inputB.in','r')
# stdout = open('outputB.in','w')

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())


queries = int_input()

for _ in range(queries):
    n = int_input()
    p = list_input()
    result = []
    for i in p:
        count = 1
        book = p[i-1]
        initial = i
        while book!=i:
            book = p[book-1]
            count+=1
        result.append(count)
    for i in result:
        print(i,end = ' ')
    print()


