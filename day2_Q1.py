a=list(map(int,(input('Enter the numbers: ').split())))
b=[]
c=[]
for i in a:
    if i not in b:
        b.append(i)
    elif i not in c:
        c.append(i)
d=sorted(b)
print('Unique(sorted) :',d)
print('Duplicates found :',c)