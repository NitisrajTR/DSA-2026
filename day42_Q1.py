a=int(input('Enter size of matrix: '))
b=[]
s=0
for i in range(a):
    c=list(map(int,(input('Enter elements of row separated by space: ').split())))
    b.append(c)
for j in range(len(b)):
    s=s+b[j][j]
print(s)