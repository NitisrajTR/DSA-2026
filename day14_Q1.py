a=list(map(int,(input('Enter Sorted Array: ').split())))
t=int(input('Enter the Target element: '))
s=0
z=len(a)
h=z-1
l=0
m=(l+h)//2
while l<=h:
    if a[m]==t:
        break
    elif a[m]<t:
        l=m+1
    else:
        h=m-1
    m=(l+h)//2
h=0
l=0
for i in range(z):
    if m-i<0 or a[m-i]!=t:
        break
    elif a[m-i]==t:
        l=m-i
for i in range(z):
    if m+i>=z or a[m+i]!=t:
        break
    elif a[m+i]==t:
        h=m+i
if a[m]==t:
    print('First index:',l)
    print('Last index:',h)
    print('Total Occurrences:',h-l+1)
else:
    print('First index:',-1)
    print('Last index:',-1)
    print('Total Occurrences:',0)