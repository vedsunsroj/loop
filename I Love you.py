r=1
while r<=5:
	c=1
	while c<=14:
		if (r==1 and c==1) or (r==1 and c==2) or (r==1 and c==3) or (r==1 and c==5) or (r==1 and c==6) or (r==1 and c==8) or ( r==1 and c==9) or (r==1 and c==11) or (r==1 and c==14):
			print("*",end=" ")
		elif ( r==2 and c==2) or (r==2 and c==4) or (r==2 and c==7) or (r==2 and c==10) or (r==2 and c==11) or ( r==2 and c==14):
			print("*",end=" ")
		elif (r==3 and c==2) or (r==3 and c==5) or (r==3 and c==9) or (r==3 and c==11) or (r==3 and c==14):
			print("*",end=" ")
		elif (r==4 and c==2) or (r==4 and c==6) or (r==4 and c==8) or (r==4 and c==11) or (r==4 and c==14):
			print("*",end=" ")
		elif (r==5 and c==1) or (r==5 and c==2) or ( r==5 and c==3) or (r==5 and c==7) or (r==5 and c==11) or (r==5 and c==12) or (r==5 and c==13) or (r==5 and c==14):
			print("*",end=" ")	
		else:
			print(" ",end=" ")
		c+=1
	print()
	r+=1