a=list(map(int,(input('Enter numbers separated by space: ').split())))
z=min(a)
y=min(a)
x=[]
w=[]
for i in range(len(a)):
    b=1
    for j in range(len(a)):
        w.append(z)
        z=z+1
        if z in a:
            b=b+1
        else:
            break
    x.append(b)
    for i in range(len(a)):
        y=a[i]
        if y in a and y not in w:
            z=y
            break
        else:
            continue
    else:
        break
print(max(x))
