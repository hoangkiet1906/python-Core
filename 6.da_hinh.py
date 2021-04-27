class bo:
	def di(self):
		print("Di = 4c")
	def da(self):
		print("Da mau nau")
class trau(bo):
	def da(self):
		print("Da mau den")
ConBo = bo()
ConTrau = trau()
print("Bo")
ConBo.di()
ConBo.da()
print("Trau")
ConTrau.di()
ConTrau.da()