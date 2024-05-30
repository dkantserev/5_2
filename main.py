obj=input()
r=''
if len(obj)>1000:
	print('max 1000 letters')
	exit()
	
for i in range(0,len(obj),1):
	
	if obj[i]==' ' and obj[i-1]!=' ':
		r=r+obj[i]
		
	elif obj[i]!=' ':
		r=r+obj[i]
		
print(r)
