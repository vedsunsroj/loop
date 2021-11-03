num=int(input("enter your number"))
start=1
count=0
while start<num:
		if num%start==0:
				count=count+start
		start=start+1
if count==num:
	print("perfect")
else:
	print("not")


i=1
while i<=100:
	j=1
	sum=0
	while j<i:
		if i%j==0:
			sum=sum+j
		j=j+1
	if sum==i:
		print(i)
	i=i+1