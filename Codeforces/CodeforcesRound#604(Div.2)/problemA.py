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
chars = ['a','b','c','?']

for _ in range(test):
    
    flag = 0
    string = string_input()
    string = string.strip()
    #print(len(string))
    new = ""
    for i,ch in enumerate(string):
        x = chars
        if ch == '?':
            left = ''
            right = ''
            if i-1 >=0:
                left = x.index(string[i-1])
            if i+1<len(string):
                right = x.index(string[i+1])
            character = ''
            k = 0
            for j in range(len(x)):
                if j!=left and j!= right and j!=3:
                    character = j
                    break
            #print(x[character])
            string = string[:i]+x[character]+string[i+1:]
        else:
            left = ''
            right = ''
            if i-1 >=0:
                left = string[i-1]
            if i+1<len(string):
                right = string[i+1]
            if left == ch or right == ch:
                flag = 1
                break

    if flag == 0:
        print(string)
    else:
        print(-1)
            