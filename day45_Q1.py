a=int(input('Enter size of matrix: '))
b=[]
for i in range(a):
    c=list(map(int,(input('Enter elements of row separated by space: ').split())))
    b.append(c)
z=0
for i in range(len(b)):
    for j in range(len(b[i])):
        if b[i][j]==b[j][i]:
            z=z+1
            continue
        else:
            z=0
            break
    if z==0:
        break
if z==0:
    print('NO')
else:
    print('YES')