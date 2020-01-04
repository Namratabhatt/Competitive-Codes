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

n = int_input()
input_arrays = []
first_digit = []
accent = [False]*n
total_accent = 0
nas = 0
def check(arr):
    if len(arr) == 1:
        return False
    else:
        for i in range(1, len(arr)):
            if arr[i]>arr[i-1]:
                return True
        return False

maxi= [0]*1000001
big = []
small= []

for _ in range(n):
    input_ = list_input()
    size = input_[0]
    input_arrays.append(input_[1:])
    accent[_] = check(input_[1:])
    total_accent += int(accent[_])
    if accent[_] == False:
        nas+=1
        big.append(max(input_[1:]))
        small.append(min(input_[1:]))

ans = 0

ans += total_accent*total_accent
ans+=total_accent*(2*nas)

for i in big:
    maxi[i]+=1

for i in range(999999,-1,-1):
    maxi[i] += maxi[i+1]

for i in small:
    ans+=maxi[i+1]

#print(nas,total_accent)
print(ans)

                
    
