n=int(input("enter a number"))
i=1
c=0
while i<=n:
	if n%i==0:
		c=c+1
	i=i+1
if c==2:
	print("it is prime")
else:
	print("it is not prime")


n=1
while n<=100:
	sum=0
	i=1
	while i<=100:
		if n%i==0:
			sum+=1
		i+=1
	if sum==2:
		print(n)
	n+=1