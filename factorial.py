
def fact(n):
	f=1
	for i in range(1,n+1):
		f=f*i

	return f





num=int(input("Enter the number for calculating factorial "))
result=fact(num)

print(result)