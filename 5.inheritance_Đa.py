class cha1:
	def __init__(self,nha):
		self.n=nha
class cha2:
	def __init__(self,xe):
		self.x=xe
class con(cha1,cha2):
	def __init__(self,nha,xe,tien):
		cha1.__init__(self,nha)
		cha2.__init__(self,xe)
		self.t=tien
chaA=cha1("Nhà Đẹp")
print("Cha1 có :"+chaA.n)
chaB=cha2("Ferrari")
print("Cha2 có xe :"+chaB.x)
kiet=con(chaA.n,chaB.x,500)
print("Kiệt chỉ có tiền nhưng kế thừa từ cha1 và cha 2 nên có \n"+kiet.n+" với Xe "+kiet.x+"\nSố tiền là : "+str(kiet.t))
