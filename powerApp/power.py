def power(a,b):
	if(b==1):
		return b
	if (b<0):
		raise ValueError("b cant be a negative value")
	if(b !=1 and b>0):
		return (a*pow(a,b-1))
print(power(3,2))
print(power(2,3))

