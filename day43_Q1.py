a=int(input('Enter size of matrix: '))
b=[]
for i in range(a):
    c=list(map(int,(input('Enter elements of row separated by space: ').split())))
    b.append(c)
z=[]
for j in range(len(b)):
    z.append([])
for j in b:
    y=0
    for i in j:
        z[y].append(i)
        y=y+1
print(z)