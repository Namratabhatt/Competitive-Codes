from math import sqrt

MOD = pow(10,9)+7
MAX= 10e+9

class Point:
    def __init__(self,x,y,distOrigin,distEnd):
        self.x = x
        self.y = y
        self.distOrigin = distOrigin
        self.distEnd = distEnd

test = int(input())

def distance(a,b,c,d):
    return sqrt( ((a-c)*(a-c)) + ((b-d)*(b-d)) )


for _ in range(test):
    x,y = map(int,input().split())
    origin = Point(x,y,MAX,MAX)
    n,m,k = map(int,input().split())
    Set1 = []
    Set2 = []
    Set3 = []
    s1 = [int(x) for x in input().split()]
    s2 = [int(x) for x in input().split()]
    s3 = [int(x) for x in input().split()]

    for i in range(0,2*n-1,2):
        Set1.append(Point(s1[i],s1[i+1],MAX,MAX))
    for i in range(0,2*m-1,2):
        Set2.append(Point(s2[i],s2[i+1],MAX,MAX))
    for i in range(0,2*k-1,2):
        Set3.append(Point(s3[i],s3[i+1],MAX,MAX))

    for i in Set1:
        minDistance = 10e+9
        for j in Set3:
            dist =  distance(i.x,i.y,j.x,j.y)
            if dist<minDistance:
                minDistance = dist
                i.distEnd = minDistance

    nearestSet2 = {}
    for i in Set2:
        minDistance = 10e+9
        for j in Set3:
            dist =  distance(i.x,i.y,j.x,j.y)
            if dist<minDistance:
                minDistance = dist
                i.distEnd = minDistance

    distSet1FromStart = {}
    for i in Set1:
        i.distOrigin = distance(x,y,i.x,i.y)

    distSet2FromStart = {}
    for i in Set2:
        i.distOrigin = distance(x,y,i.x,i.y)
    


    #print(nearestSet1)
    mini = 10e+9
    for i in Set1:
        for j in Set2:
            distBetweenPoints = distance(i.x,i.y,j.x,j.y)
            dist1 = i.distOrigin + distBetweenPoints
            dist2 = j.distOrigin + distBetweenPoints
            setC1 = dist1 + j.distEnd
            setC2 = dist2 + i.distEnd
            if setC1<mini:
                mini = setC1
            if setC2<mini:
                mini = setC2

    print ('%.7f'%mini)          
