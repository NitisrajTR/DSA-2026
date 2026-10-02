a=list(map(int,(input('Enter Sorted Array: ').split())))
t=int(input('Enter the element to be searched: '))
s=0
z=len(a)
h=z-1
l=0
m=(l+h)//2
while l<=h:
    if a[m]==t:
        s=s+1
        break
    elif a[m]<t:
        l=m+1
    else:
        h=m-1
    m=(l+h)//2
    s=s+1
if a[m]==t:
    print('Index:',m)
else:
    print('Element not found')
    print('Index:',-1)
print('Steps:',s)