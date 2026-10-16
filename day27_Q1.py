a=list(map(int,(input('Enter numbers separated by space: ').split())))
n=int(input('Enter the target sum: '))
b=[]
c=[]
l=0
r=0
while r<len(a) or len(b)>0:
    if sum(b)<n and r<len(a):
        b.append(a[r])
        r=r+1
    elif sum(b)>=n:
        c.append(len(b))
        l=l+1
        b.pop(0)
    else:
        break
if len(c)>0:
    print('Best length:',min(c))
else:
    print('Best length: 0')