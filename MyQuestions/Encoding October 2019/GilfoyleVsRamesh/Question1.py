from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
import os
import sys
int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

textfiles = 1


def check_composite(n, a, d, s):
	x = pow(a, d, n)
	if x==1 or x==n-1:
		return False
	for r in range(1, s):
		x = x * x % n
		if x==n-1:
			return False
	return True

def miller_rabin(n):
	if n<2:
		return 0
	r = 0 
	d = n-1
	while((d&1)==0):
		d >>=1
		r += 1
	base = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
	for a in base:
		if n==a:
			return 1
		if check_composite(n, a, d, r):
			return 0
	return 1

for i in range(textfiles):

	#stdin = open(os.path.join(sys.path[0],'input0.in'),'r')
	# sys.stdout = open(os.path.join(sys.path[0],('testfile_output'+str(i)+'.in')),'w')

	# test = int_input()
	# for _ in range(test):

	n = int_input()
	input_array = list_input()

	first_prime = -2
	last_prime = -2

	leftCount = 0
	rightCount = 0

	for i in range(n//2):
		if (miller_rabin(input_array[i]) == 1):
			if first_prime == -2:
				first_prime = input_array[i]
			#print(input_array[i])
			leftCount+=1
	
	for i in range(n//2,n):
		if (miller_rabin(input_array[i]) == 1):
			last_prime = input_array[i]
			#print(input_array[i])
			rightCount+=1

	#print(leftCount,rightCount,first_prime,last_prime)
	if (leftCount == rightCount and first_prime>last_prime):
		print('PERFECT')
	else:
		print('IMPERFECT')
