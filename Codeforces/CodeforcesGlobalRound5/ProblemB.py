from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

n = int_input()

input_sequence = list_input()
output_sequence = list_input()

fines= 0

state_car = {}

for i in range(1,n+1):
    state_car[i] = 0

k = 0
l = 0
while(k<len(input_sequence)):
    if state_car[input_sequence[k]] == 1:
        k+=1
    else:
        if input_sequence[k]!=output_sequence[l]:
            state_car[output_sequence[l]] = 1
            l+=1
            fines+=1
        else:
            l+=1
            k+=1

print(fines)
