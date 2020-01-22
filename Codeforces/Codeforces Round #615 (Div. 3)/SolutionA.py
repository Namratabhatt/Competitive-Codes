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
    a,b,c,n = multi_int_input()
    if a == b  and b == c and n%3 == 0:
        print("YES")
    else:
        maxi = 0
        if a>=b and a>=c:
            maxi = a
        elif b>=a and b>=c:
            maxi = b
        else:
            maxi = c

        diff = maxi - a + maxi - b +maxi - c
        n = n - diff
        if n<0:
            print("NO")
        else:
            if n%3 == 0:
                print("YES")
            else:
                print("NO")
