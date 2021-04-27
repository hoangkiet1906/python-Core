import collections
d1 = collections.OrderedDict()
d1['A']=10
d1['B']=12
d1['C']=13
d1['D']=14
d1['C']=15
for i,x in d1.items():
	print(i,x)
