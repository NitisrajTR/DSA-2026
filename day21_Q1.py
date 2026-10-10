a=list(map(int,(input('Enter numbers separated by space: ').split())))
b=[]
b.append(a[-1])
c=[-1]
for i in range(len(a)-1):
    if len(b)>0 and a[-i-2]<b[-1]:
        c.append(b[-1])
        b.append(a[-i-2])
    else:
        if len(b)>0:
            z=b.pop()
            while len(b)>0:
                if a[-i-2]<b[-1]:
                    c.append(b[-1])
                    b.append(a[-i-2])
                    break
                else:
                    z=b.pop()
            else:
                c.append(-1)
                b.append(a[-i-2])
        else:
            c.append(-1)
            b.append(a[-i-2])
c.reverse()
print(*c)