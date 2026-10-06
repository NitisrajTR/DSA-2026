a=list(map(int,(input('Enter sorted numbers separated by space: ').split())))
s=0
f=0
for i in range(len(a)-1):
    f=f+1
    if a[f]==a[s]:
        continue
    else:
        s=s+1
        a[s]=a[f]
print('Length',s+1)
print('List',a[:s+1])