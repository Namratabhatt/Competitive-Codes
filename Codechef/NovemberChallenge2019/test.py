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


def sum_of(array,index):
    sum = 0
    for i in range(index):
        sum+=array[i]
    return sum

test = int_input()
for _ in range(test):
    n = int_input()
    c = [0]*n
    input_list = [0]*n

    for x in range(n):
        temp = list_input()
        c[x] = temp[0]
        input_list[x] = temp[1:]

    max_sum = 0
    odd_sums_frst= []
    odd_sums_last = []
    for i in range(n):
        if c[i]%2 == 0:
            max_sum+=sum_of(input_list[i],c[i]//2)
        else:
            odd_sums_frst.append([(sum_of(input_list[i],c[i]//2+1)),sum_of(input_list[i],c[i]//2)])

    sorted_odd_sums_first = sorted(odd_sums_frst,reverse=True)

    for i in range(len(sorted_odd_sums_first)):
        if i%2 == 0:
            max_sum+=sorted_odd_sums_first[i][0]
        else:
            max_sum+=sorted_odd_sums_first[i][1]
    
    print(max_sum)