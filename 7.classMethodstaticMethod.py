class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	@classmethod
	def Cach1(cls,name,year):
		return cls(name,2021-year)
	@staticmethod
	def Ktr18(age):
		return age>18
kiet = Person("Kiet",17)
print(kiet.name+" "+str(kiet.age)+" tuổi")
print(kiet.Ktr18(kiet.age))
print(Person.Ktr18(kiet.age))

kiet = Person.Cach1("Kiệt",2002)
print(kiet.name+" "+str(kiet.age)+" tuổi")
print(kiet.Ktr18(kiet.age))
print(Person.Ktr18(kiet.age))
