class person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
class sinhvien(person):
	def __init__(self,name,age,lop):
		super().__init__(name,age)
		self.lop=lop
Obama = person("Obama",50)
Kiet = sinhvien("Kiet",18,"20it1")
print(Obama.name,Obama.age)
print(Kiet.name,Kiet.age,Kiet.lop)