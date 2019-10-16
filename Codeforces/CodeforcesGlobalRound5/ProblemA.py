from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import ceil,floor

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

n = int_input()
final_ratings = []
last_index = 0
counter = 0
index_of_odd = []
initial_ratings = []
for i in range(n):
    score = int_input()
    if score%2 == 0:
        score = score//2
    else:
        score = score/2
        if score<0:
            score = int(floor(score))
        else:
            score = int(floor(score))
        index_of_odd.append(i)
    final_ratings.append(score)

sum = 0
for i in final_ratings:
    sum+=i

#print(*final_ratings)

k = 0
while sum!=0:
    if sum<0:
        final_ratings[index_of_odd[k]]+=1
        sum+=1
        k+=1

for i in final_ratings:
    print(i)
