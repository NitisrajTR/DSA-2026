a=list(map(int,(input('Enter numbers separated by space: ').split())))
t=int(input('Enter Target number: '))
b={}
c=[]
for i in range(len(a)):
    x=a[i]
    z=t-x
    if z not in b:
        b[x]=i
    else:
        print('Indices:',b[z],i)
        c.append((b[z],i))
        break
if len(c)==0:
    print('Indices: -1')