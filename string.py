string=input("enter a string")
li=[]
for char in string:
    if char not in l:
        l.append(char)
res=''.join(l)
print(res)
print(type(res))
l=['T','H','A','R','U','N']
res=''.join(l)
print(res)
print(type(res))