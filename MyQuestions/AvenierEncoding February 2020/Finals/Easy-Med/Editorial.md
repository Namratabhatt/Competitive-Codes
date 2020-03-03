
[Practice](https://www.codechef.com/ENFE2020/problems/ECFEB204)
[Encoding February 2020 Finals Contest](https://www.codechef.com/ENFE2020?itm_campaign=contest_listing)

***Author:***  [arnie8991](https://www.codechef.com/users/arnie8991)
***Tester:***  [nutella](https://www.codechef.com/users/nuttela)
***Editorialist:***  [arnie8991](https://www.codechef.com/users/arnie8991)

# DIFFICULTY:
Easy-Medium

# PREREQUISITES:
Maths, Sorting, Greedy
 
# EXPLANATION:

We have been asked to find the order of the citites that Imran should visit so that he gets to visit the maximum number of his friends in ascending order. The easiest and intuitive approach is to choose the diagonal with the biggest sum and sort number of friends that mran has in that diagonal and then print them in the order as mentioned in the input grid. For that sake of convenience, a priority queue has been used here to sort all the diagonal elements automatically.

# SOLUTIONS:

[details="Setter's Solution"]

row = col = int(input())

grid = []*row 

for i in range(row):
    grid.append([int(x) for x in input().split()])

dictionary = {}

for i in range(row):
    for j in range(col):
        if i-j not in dictionary:
            dictionary[i-j] = [0,[]]
            heapq.heapify(dictionary[i-j][1])

for i in range(row):
    for j in range(col):
        dictionary[i-j][0]+=grid[i][j]
        heapq.heappush(dictionary[i-j][1],grid[i][j])

maxi = None
high = -1000
key = None
for items in dictionary:
    if dictionary[items][0]>high:
        maxi = dictionary[items][1]
        high = dictionary[items][0]
        key = items


original = []
for i in range(row):
    for j in range(col):
        if i-j == key:
            original.append([grid[i][j],i,j])

while(len(maxi)>0):
    ele = heapq.heappop(maxi)
    for items in original:
        if items[0] == ele:
            print(items[1],items[2])

[details="Tester's Solution"]
