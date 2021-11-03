i=int(input("enter a number"))
sum=0
x=i
while i>0:
	a=i%10
	sum=sum+a
	i=i//10
if x%sum==0:
	print("harshad")
else:
	print("not harshad")



i=1
while i<=100:
    x=i
    sum=0
    while x>0:
        a=x%10
        x=x//10
        sum=a+sum
    if i%sum==0:
        print(i)
    i+=1