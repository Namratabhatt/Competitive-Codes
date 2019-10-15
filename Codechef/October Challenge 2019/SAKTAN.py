from math import gcd 
from collections import defaultdict, deque
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_input =lambda : map(int, stdin.readline().split())
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

test = int_input()
for i in range(test):
    n,m,q = multi_input()

    freq_row = {}
    freq_col = {}

    for i in range(n):
        freq_row[i+1] = 0
    
    for i in range(m):
        freq_col[i+1] = 0

    for i in range(q):
        row,col = multi_input()
        freq_row[row] +=1
        freq_col[col] +=1

    count = 0

    row_even = 0
    row_odd = 0

    for i in freq_row:
        if(freq_row[i]%2 == 0):
            row_even +=1
        else:
            row_odd +=1
    
    for i in freq_col:

        if(freq_col[i]%2==0):
            count+=row_odd
        else:
            count+=row_even

    print(count)
