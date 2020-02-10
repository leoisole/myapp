print("enter no. of elements:")
num = int(input())


a = []
while num != 0 :
	print("enter the data:")
	a.append(int(input()))
	num = num-1

print("How many times you want to rotate : ")

time = int(input()) 
temp = a[:-(time+1):-1]
print(temp)
temp.reverse()
res = temp + a[0:num-time]
print(res)

