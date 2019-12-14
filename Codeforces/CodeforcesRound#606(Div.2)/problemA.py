from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
import os,sys
int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7
# stdin = open(os.path.join(sys.path[0],'input.in'),'r')
# sys.stdout = open(os.path.join(sys.path[0],'output2.in'),'w')
test = int_input()
arr = [9,18,27,36,45,54,63,72,81]
for _ in range(test):

    n = int_input()

    if n<=9:
        print(n)
    else:
        string_no = str(n)
        length_no = len(string_no)
        first_digit = int(string_no[0])
        maximum = str(first_digit)*length_no
        maximum = int(maximum)
        if maximum<=n:
            print(arr[length_no-2]+first_digit)
        else:
            print(arr[length_no-2]+(first_digit-1))
        
