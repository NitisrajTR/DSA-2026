a=list(map(int,(input('Enter no of steps separated by space: ').split())))
j=0
for i in range(len(a)):
    if i>j:
        break
    j=max(j,i+a[i])
if j>=len(a)-1:
    print('Yes')
else:
    print('No')