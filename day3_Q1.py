a=list(map(int,(input('Enter numbers of list 1:').split())))
b=list(map(int,(input('Enter numbers of list 2:').split())))
c=[]
for i in a:
    if i in b:
        c.append(i)
d=[]
for i in a:
    if i not in c:
        d.append(i)
e=[]
for i in b:
    if i not in c:
        e.append(i)
f=c+d+e
c.sort()
d.sort()
e.sort()
f.sort()
print('Common (intersection):',c)
print('Only in list 1:',d)
print('Only in list 2:',e)
print('Union:',f)