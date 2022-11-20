# import re
# f=open('txt.txt','r')
# a=f.readlines()
file=open('txt.txt', 'r')
a=file.read()
b=a
b=b.split()
# c=b.find('@bebra')
for i in range(len(b)):
	if b[i]=='@antoo':
		int1=int(b[i+1])
		b[i+1]='200'
a=open('txt.txt','w')		
for i in range(len(b)):
	try:
		a.write(b[i]+' '+b[i+1])
	except IndexError:
		pass 
print(b)