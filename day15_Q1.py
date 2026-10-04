a=list(map(int,(input('Enter Rotated Sorted Array: ').split())))
t=int(input('Enter the Target element: '))
b=[]
l=0
h=len(a)-1
m=(l+h)//2
if t not in a:
    print('Element not found')
    print('Index:',-1)
else:
    while a[m]!=t:
        if a[m]>t:
            b=a[l:m+1]
            b.sort()
            if t in b:
                h=m-1
            else:
                l=m+1
        elif a[m]<t:
            b=a[m:h+1]
            b.sort()
            if t in b:
                l=m+1
            else:
                h=m-1
        m=(l+h)//2
    print('Index',m)