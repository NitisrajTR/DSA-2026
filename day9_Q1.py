z=input('String:')
a=z.lower()
a=a.replace(' ', '')
b=[]
c=len(a)
for i in range(c):
    for j in range(c):
        if a[i] not in b:
            if j>i:
                if a[i]==a[j]:
                    b.append(a[i])
            else:
                continue
d=[]
for i in a:
    if i not in b:
        d.append(i)
if len(d)==0:
    print('No non-repeating character found')
else:
    print('The first non-repeating character is:',d[0])