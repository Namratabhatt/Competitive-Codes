from math import gcd 
from collections import defaultdict, deque
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_input =lambda : map(int, stdin.readline().split())
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

test = int_input()
for i in range(test):
    n,k = multi_input()
    sequence = list_input()
    dictionary = {}

    if(k<(3*n)):
        for i in range(0,k):
            posa = i%n
            posb = n - (i%n) - 1
            a = sequence[i%n]
            b = sequence[n - (i%n) - 1]

            sequence[i%n] = a^b
            print("New sequence is: ",*sequence,"for i:",i,"and cycle is : ",i//n,i%n)
    else:
        for i in range(n):
            dictionary[i] = []

        for i in range(0,3*n):
            posa = i%n
            posb = n - (i%n) - 1
            a = sequence[i%n]
            b = sequence[n - (i%n) - 1]    
            sequence[i%n] = a^b
            dictionary[i%n].append(a^b)

        #print(dictionary)
        cycle = ((k-1)//n) %3
        #print(cycle,(k-1)%n)
        for i in range(0,n):
            if(i <= ((k-1)%n)):
                sequence[i] = dictionary[i][(cycle)%3]
            else:
                sequence[i] = dictionary[i][(cycle-1)%3]

    print(*sequence)