a=list(map(int,(input('Enter the elements of the array separated by space: ').split())))
x=int(input('Enter the Target element: '))
b=[]
for i in range(len(a)):
    if a[i]==x:
        b.append(i)
c=len(b)
if len(b)==0:
    print('First index found:',[-1])
else:
    print('First index found:',b[0])
print('Total occurrences:',c)
print('All indices found:',b)