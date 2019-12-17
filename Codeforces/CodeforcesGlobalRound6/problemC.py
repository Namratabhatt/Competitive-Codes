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

r,c  = multi_int_input()

if r == 1 and c == 1:
    print(0)
elif  r==1 and c>1:
    base = 2
    result = [base+i for i in range(c)]
    print(*result)
elif r>1 and c == 1:
    base = 2
    for i in range(r):
        print(base+i,end = " ")
    print()
else:
    result_row = []
    for i in range(1,r+1):
        result_row.append(i)
    result_col = []
    for i in range(r+1,r+c+1):
        result_col.append(i)
    final = []
    for i in range(r):
        final.append([])
        for j in range(c):
            final[i].append(0)
    for i in range(r):
        for j in range(c):
            final[i][j] = result_row[i]*result_col[j]

    for i in range(r):
        for j in range(c):
            print(final[i][j],end =" ")
        print()