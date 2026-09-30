a=list(map(int,(input('Enter the elements of the array separated by space: ').split())))
b=a[0::]
c=[]
s=0
z=min(a)
for i in range(len(a)):
    for j in range(len(a)):
        y=a.index(z)
        if i==y:
            b.clear()
            b=a[i+1::]
            if len(b)>0:
                z=min(b)
            break
        else:
            a[i],a[y]=a[y],a[i]
            s=s+1
            b.clear()
            b=a[i+1::]
            if len(b)>0:
                z=min(b)
            break
print('Sorted list:',a)
print('Total swaps:',s)