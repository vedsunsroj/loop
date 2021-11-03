i=1
sum=0
while i<=11:
	n=int(input("enter any weight"))
	sum=sum+n
	i+=1
a=sum/11
print('sum ',sum,' average ',a)
if a%5==0:
	print("divisible h")
else:
	print("nhi h")