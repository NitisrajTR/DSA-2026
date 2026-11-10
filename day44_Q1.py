a=int(input('Enter size of matrix: '))
b=[]
for i in range(a):
    c=list(map(int,(input('Enter elements of row separated by space: ').split())))
    b.append(c)
z=[]
for j in range(len(b)):
    z.append([])
w=0
for j in b:
    y=0
    for i in range(len(j)):
        x=a-1-y
        z[w].append(b[x][w])
        y=y+1
    w=w+1
for i in z:
    print(*i)