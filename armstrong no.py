i=int(input("enter a no"))
x=i
sum=0
while i>0:
	sum=sum+(i%10)(i%10)(i%10)
	i=i//10
if sum==x:
	print("number is armstrong")
else:
	print("number is not armstrong")


