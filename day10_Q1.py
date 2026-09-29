a=list(map(int,(input('Enter the elements of the array separated by space: ').split())))
n=len(a)
s=0
for i in range(n):
    for j in range(n-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            s+=1
print('Sorted list:',a)
print('Total swaps:',s)