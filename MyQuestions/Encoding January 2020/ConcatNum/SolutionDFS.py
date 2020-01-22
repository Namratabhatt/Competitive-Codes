'''

This is the solution using dfs and bruteforce

'''

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
string_list_input=lambda: list(string_input().split())
MOD = pow(10,9)+7
import os,sys

sys.setrecursionlimit(10000)

stdin = open(os.path.join(sys.path[0],'input4.in'),'r')
sys.stdout = open(os.path.join(sys.path[0],'output4.in'),'w+')

def isConcatenated(hashset,number,index):

    word = number[index:]
    for i in range(1,len(word)):
        if word[:i] in hashset:
            
            if word[i:] in hashset or isConcatenated(hashset,number,index+i):
                return True
    return False

def solution(list_):
    concatenated = []
    hashset = set([])

    for numbers in list_:
        hashset.add(numbers)

    for numbers in list_:
        if isConcatenated(hashset,numbers,0):
            concatenated.append(numbers)
    

    print(len(concatenated))


n = int_input()

list_ = string_list_input()

solution(list_)