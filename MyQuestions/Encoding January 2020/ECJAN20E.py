test = int(input())
for _ in range(test):
	a,b = map(int,input().split())
	if (a == 1 or a == 3 or a == 7 or a == 9) and b!= 5:
		print('sheldon')
	elif (a == 1 or a == 3 or a == 7 or a == 9) and b== 5:
		print('draw')
	elif (a == 5) and b%2 == 0:
		print('sheldon')
	else:
		print('draw')
