def cp():
	i=1
	while True:
		yield i*i
		i+=1
for i in cp():
	print(i)
	if(i>100):
		break