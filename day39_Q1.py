a=list(map(int,(input('Enter Time separated by space: ').split())))
c=[]
for i in range(len(a)):
    b=[]
    if i%2==0:
        b=a[i:i+2:]
        c.append(b)
def get(i):
    return i[1]
c.sort(key=get)
l=-1
d=0
for i,j in c:
    if i>=l:
        d=d+1
        l=j
print(d)