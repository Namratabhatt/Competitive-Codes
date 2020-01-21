'''

A solution using Tries

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

class Trie:
    def __init__(self):
        self.array = [None]*10
        self.isNumber = False


def buildTrie(root,number):
    current = root
    for c in number:
        index  = ord(c) - ord('0')
        if( current.array[index] == None ):
            current.array[index] = Trie()
        current = current.array[index]
    current.isNumber = True

def search(root,number,begin,num):
    current = root;
    for i in range(begin,len(number)):
        index = ord(number[i]) - ord('0')
        if( current.array[index] == None ):
            return False
        current = current.array[index]
        if( current.isNumber and search(root, number, i + 1, num + 1) ) :
            return True
    return num >= 1 and current.isNumber

def solution(list_):

    root = Trie()
    for numbers in list_:
        if len(numbers)>0:
            buildTrie(root,numbers)

    result = []
    
    for number in list_:
        if( search(root, number, 0, 0) ):
            result.append(number)

    print(len(result))

n = int_input()

list_ = string_list_input()

solution(list_)