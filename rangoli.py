

#n = 3
alp = "abcdefghijklmnopqrstuvwxyz"
print(alp)
n = int(input())
a = "".join(alp[0:n])
data = []

for i in range(2*n-1):
	data.append([])
	for j in range(2*n-1) :
		data[i].append("-")


buffer = [[n-1,n-1]]


for i in a:
	item = []
	for j in buffer :
		#print(j,type(j),"j")
		item.append([j[0]-1,j[1]])
		item.append([j[0]+1,j[1]])
		item.append([j[0],j[1]-1])
		item.append([j[0],j[1]+1])
		#print("item",item)
		#print(j,type(j),"asd")
		#print(j[0],j[1],"abh")
		#print("data",data)
		if data[j[0]][j[1]] == '-' :
			print("asd")
			data[j[0]][j[1]] = i

	buffer=item
	
for d in data:
	print(d)
			
	
