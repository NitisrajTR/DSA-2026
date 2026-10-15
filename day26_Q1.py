a=input('Enter the string: ')
b=list(a)
c=[]
d=[]
r=0
l=0
n=0
if len(b)==0:
    print('Length: 0')
else:
    r=0
    l=0
    n=0
    while r<len(b):
        if b[r] not in c:
            c.append(b[r])
            r=r+1
            n=len(c)
            d.append(n)
        else:
            c.pop(0)
            l=l+1
            n=len(c)
    print('Length:',max(d))