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
    def init(self,id,score):
        self.id = id
        self.score = score

class Library:
    def init(self,id,numberB,signupT,freq,books,books_scanned,number_of_books):
        self.id = id
        self.numberB = numberB
        self.signupT = signupT
        self.freq = freq
        self.books = books
        self.books=books_scanned
        self.number_of_books=number_of_books
        

input_files = ["a_example.txt"]
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
        books_scanned=[]
        number_of_books=0
        for id in ids:
            bobj = Books(id,B_scores[id])
            books.append(bobj)

        libObj = Library(i,N,T,M,books,books_scanned,number_of_books)
        Libraries.append(libObj)
    
    for library in Libraries:
        # print(library.books)
        library.books.sort(key = lambda x: x.score, reverse = True)

    Libraries.sort(key = lambda x: x.signupT)
    
    signup = 0
    working_on = 0
    Lib_index = 0
    
    included_lib = []
    # print(len(Libraries),"Length of lib")
    while(working_on<=D and Lib_index<len(Libraries)):
        curr_lib = Libraries[Lib_index]
        working_on+=curr_lib.signupT
        # print("Hello",curr_lib.signupT)
        included_lib.append(curr_lib)
        Lib_index+=1
    new_included=[]
    print(len(included_lib))
    # print(included_lib)
    i=0
    for librarie in included_lib:
        # print(librarie.books)
        librarie.books.sort(key = lambda x: map_books[x.id],reverse = True)
        print(librarie.id,librarie.numberB)
        books_scanned = []
        i+=librarie.signupT
        temp=i+1
        k=0
        while(temp<=D and k<len(librarie.books)):
            x=0
            while(x<librarie.freq and  temp<=D ):
                books_scanned.append(librarie.books[k].id)
                map_books[librarie.books[k].id]=0
                x+=1
                k+=1
            temp+=1
        librarie.books_scanned=books_scanned
        librarie.number_of_books=k
        if(k!=0):
            new_included.append(librarie)
    print(len(included_lib))
    for lib in new_included:
        print(lib.id,lib.number_of_books)
        print(*books_scanned)

        
