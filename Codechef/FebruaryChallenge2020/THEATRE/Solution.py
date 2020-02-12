from sys import stdin,stdout

intinp=lambda : int(stdin.readline())
multi_int =lambda : map(int, stdin.readline().split())
lstinp=lambda : list(map(int,stdin.readline().split()))

test = intinp()
final_ans = 0

mapperTime = {12:0,3:1,6:2,9:3}
mapperMovie = {'A':0,'B':1,'C':2,'D':3}


possible = []

for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if len(set([i,j,k,l])) == 4:
                    possible.append([i,j,k,l])

def computescore(array):
    # print(array)
    array.sort(reverse = True)
    ini = 100
    score = 0
    for i in array:
        if i == 0:
            score-=100
        else:
            score+=(ini*i)
            ini-=25
    # print(score)
    return score


for _ in range(test):
    ans = 0

    n = intinp()
    
    twoD = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(n):
        movie,time = stdin.readline().split()
        time = int(time)
        twoD[mapperTime[time]][mapperMovie[movie]]+=1

    maxi = -999999
    max_combi = []
    max_data = []
    max_val = 0

    for combinations in possible:
        score = 0
        poop_arr  = []
        for i in range(4):
            poop_arr.append(twoD[i][combinations[i]])
        score = computescore(poop_arr)
        # print(score)
        if score>=maxi:
            # print("here")
            maxi = score
    
    print(maxi)

    final_ans+=maxi

print(final_ans)