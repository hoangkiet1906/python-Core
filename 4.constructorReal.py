class SieuNhan:
	def __init__(self,ten,vukhi):
		self.name=ten
		self.vk=vukhi
	def hello(self):
		return "HI Chao "+self.name
	def say_hi(self):
		print("Hi",self.name)

SieuNhanDo = SieuNhan("Do","Kiem")
print(SieuNhanDo.name)
print(SieuNhanDo.vk)

print(SieuNhan.hello(SieuNhanDo))
print(SieuNhanDo.hello())
SieuNhanDo.say_hi()

	