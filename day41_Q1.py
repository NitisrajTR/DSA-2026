a=list(map(int,(input('Enter greed values separated by space: ').split())))
b=list(map(int,(input('Enter cookies separated by space: ').split())))
a.sort()
b.sort()
c=0
for i in range(len(b)):
    if b[i] >= a[c] and c < len(a):
        c += 1
print(c)