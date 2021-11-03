i=1
while i <=50:
	if i%3==0:
		print(i,'buzz')
	if i%7==0:
		print(i,'fizz')
	if i%3==0 and i%7==0:
		print(i,'fuzz-fizz')
	i+=1