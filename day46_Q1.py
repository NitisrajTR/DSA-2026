a=int(input('Enter size of matrix: '))
b=[]
for i in range(a):
    c=list(map(int,(input('Enter elements of row separated by space: ').split())))
    b.append(c)
z=[]
m=float('-inf')
for i in b:
    s=0
    for j in i:
        s=s+j
        if s>m:
            m=s
    z.append(s)
print(z.index(m))