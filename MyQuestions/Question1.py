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

test = int_input()
import random

def exp(a,p,m):
	if (p==0):
		return 1
	elif (p%2==1):
		return (a*exp(a,p-1,m))%m
	x=exp(a,p/2,m)
	return (x*x)%m

def miller_rabin(p):

	if (p==2 or p==3):return 1
	if (p%2==0):return 0
	if (p<3):return 0

	for i in range(10):
		#random 'a'
		a = random.randrange(2,p-2)

		s=p-1
		while(s%2==0):s/=2

		mod = exp(a,s,p)
		if (mod==1 or mod==p-1):
			continue
		
		flag=0
		while(s!=(p-1)):
			mod = exp(a,s,p)
			if (mod==(p-1)):
				flag=1
				break
			s*=2
		if (flag==0):
			return 0
	return 1

for _ in range(test):

    n = int_input()
    input_array = list_input()

    first_prime = -2
    last_prime = -2

    leftCount = 0
    rightCount = 0

    for i in range(n//2):
        if (prime[input_array[i]] == True):
            if first_prime == -2:
                first_prime = input_array[i]
            leftCount+=1
    
    for i in range(n//2,n):
        if (prime[input_array[i]] == True):
            last_prime = input_array[i]
            rightCount+=1

    if (leftCount == rightCount and first_prime>last_prime):
        print("PERFECT")
    else:
        print("IMPERFECT")