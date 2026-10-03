a=list(map(int,(input('Enter the elements of the array separated by space:').split())))
s=0
for i in range(len(a)-1):
    z=a[i+1]
    for j in range(len(a)):
        y=i+1-j
        if y==0:
            break
        elif a[y]<a[y-1]:
            a[y],a[y-1]=a[y-1],a[y]
            s=s+1
        else:
            break
print('Sorted list:',a)
print('Total shifts:',s)
