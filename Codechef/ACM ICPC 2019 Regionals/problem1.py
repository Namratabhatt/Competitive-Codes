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


test  = int_input()

for _ in range(test):
    n = int_input()
    inputsequence = {}
    output = 0


    for i in range(n):

        word,valid = multi_input()

        if  word not in inputsequence:
            inputsequence[word] = [valid]
        else:
            inputsequence[word].append(valid)

    for items in inputsequence:
        if inputsequence[items].count("1")>=inputsequence[items].count("0"):
            output+=inputsequence[items].count("1")
        else:
            output+=inputsequence[items].count("0")

    print(output)