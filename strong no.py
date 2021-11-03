i=int(input("enter a no"))
n=i
sum=0
while i>0:
	x=i%10
	y=x
	fac=1
	while y>=1:
		fac=fac*y
		y-=1
	sum+=fac
	i=i//10
	
if n==sum:
	print("strong")
else:
	print("not")

