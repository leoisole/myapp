nodes = int(input("Enter the no. of nodes : "))
cost = []
for i in range(nodes) :
	cost.append([])
	for j in range(nodes):
		print("\n Enter the cost matrix for " + str([i]) + str([j]) + " node :")
		cost[i].append(int(input()))

print(cost)

src = int(input("enter the src: "))
dst = int(input("enter the dst: "))


for i in range(nodes) : #current
	
	
	for j in range(nodes) :
		
		for k in range(nodes):
			if cost[i][j] > cost[i][k] + cost[k][j] :
			
				cost[i][j] = cost[i][k] + cost[k][j]
				
print(cost)	 

print("min dist : ",cost[src][dst])	
