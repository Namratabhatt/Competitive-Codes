from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint,randrange,choice

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())

import os,sys

class Books:
    def __init__(self,id,score):
        self.id = id
        self.score = score

class Library:
    def __init__(self,id,numberB,signupT,freq,books):
        self.id = id
        self.numberB = numberB
        self.signupT = signupT
        self.freq = freq
        self.books = books

class Solution:
    def __init__(self,librarie):
        self.librarie = librarie

input_files = ["a_example.txt","b_read_on.txt","c_incunabula.txt","d_tough_choices.txt","e_so_many_books.txt","f_libraries_of_the_world.txt"]
file_name = 0
for file in input_files:
    x = file
    stdin = open(os.path.join(sys.path[0],file),'r')
    sys.stdout = open(os.path.join(sys.path[0],str(file_name)+".txt"),'w')
    file_name+=1
    
    B,L,D = multi_int_input()
    B_scores = list_input()
    map_books = {}

    for i,n in enumerate(B_scores):
        map_books[i] = n

    Libraries = []
    for i in range(L):
        N,T,M = multi_int_input()
        ids = list_input()
        books = []
        for id in ids:
            bobj = Books(id,B_scores[id])
            books.append(bobj)

        libObj = Library(i,N,T,M,books)
        Libraries.append(libObj)
    
    for library in Libraries:
        # print(library.books)
        library.books.sort(key = lambda x: x.score, reverse = True)

    Libraries.sort(key = lambda x: x.signupT)
    
    signup = 0
    working_on = 0
    Lib_index = 0
    
    included_lib = []
    Solution = []
    # print(len(Libraries),"Length of lib")
    while(working_on<=D and Lib_index<len(Libraries)):
        curr_lib = Libraries[Lib_index]
        curr_lib.books.sort(key = lambda x: map_books[x.id],reverse = True)
        if curr_lib.books[0].score>0:
            working_on+=curr_lib.signupT
            included_lib.append(curr_lib)
            Solution.append(curr_lib)
        for i in curr_lib.books:
            map_books[i.id] = 0
        Lib_index+=1

    print(len(Solution))

    for library in Solution:
        print(library.id,library.numberB)
        books = []
        for i in library.books:
            books.append(i.id)
        print(*books)