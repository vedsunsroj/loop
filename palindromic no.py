
i=int(input("enter a no"))
x=i
rev=0
while i>0:
	rev=rev*10+i%10
	i=i//10
if rev==x:
	print('palindromic')
else:
	print("not palinfromic")


name=("n","i","t","i","n")
a=name
i=-1
while i>=(-len(name)):
	   print(name[i],end=" ")
	   i=i-1
if a==name:
	print("palindromic hai")
else:
	print("nahi h")