a=list(map(int,(input('Enter heights separated by space: ').split())))
l=0
r=len(a)-1
b=0
while r>l:
    w=r-l
    m=min(a[l],a[r])
    area=w*m
    b=max(b,area)
    if a[l]>=a[r]:
        r=r-1
    else:
        l=l+1
print('Max area:',b)