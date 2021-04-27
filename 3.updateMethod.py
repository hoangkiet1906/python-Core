class myClass:
	so = 50
	@classmethod
	def update(cls,soo):
		cls.so=soo
k = myClass()
print(k.so)
#c1
k.update(30)
print(k.so)
#c2
myClass.update(20)
print(k.so)