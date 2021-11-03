i=1
sum=0
while i<=100:
	sum=sum+i
	print(i,end=" ")
	if i==100:
		break
	else:
		print('+',end=" ")
	i+=1
print("this is the sum",sum)