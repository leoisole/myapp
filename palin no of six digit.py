res = 0
a = [0,0,0,0,0,0]
def con(list) :

	s = [str(i) for i in list ]
	res = int("".join(s))
	return res

for i in range(1,10) :
	a[0] = i
	a[5] = i
	
	for j in range(0,10) :
		a[1] = j
		a[4] = j

		for k in range(0,10) :

			a[2] = k 
			a[3] = k
			num = con(a)
			print(num)


