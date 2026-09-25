a=list(map(int,(input('Enter elements of the list separated by space: ').split())))
a.sort(reverse=True)
z=a[0]
b=[]
if len(a)<3:
    print('Not enough elements(need at least 3)')
else:
    for i in a:
        if i!=z:
            b.append(i)
    b.sort(reverse=True)
    if len(b)==0:
        b=a[1:]
    y=b[0]
    c=[]
    for i in b:
        if i!=y:
            c.append(i)
    c.sort(reverse=True)
    if len(c)==0:
        c=b[1:]
    x=c[0]
    if x==y:
        print('Not enough unique elements,so 2nd and 3rd largest are same')
    print('2nd Largest:',y)
    print('3rd Largest:',x)