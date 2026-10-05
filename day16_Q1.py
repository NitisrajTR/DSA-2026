a=list(map(int,(input('Enter numbers separated by space: ').split())))
s=int(input('Enter Target sum: '))
b=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==s:
            b.append(a[i])
            b.append(a[j])
            b.append(i)
            b.append(j)
            break
        else:
            continue
    if len(b)>0:
        break
if len(b)>0:
    print('Numbers:',b[0],b[1])
    print('Indices:',b[2],b[3])
else:
    print('No pair found')
    print('Indices: -1')