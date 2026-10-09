a=list(input().split())
b=[]
for i in a:
    if i not in ['+','-','*','/','//','%','**']:
        b.append(int(i))
    else:
        r=b.pop()
        l=b.pop()
        if i=='+':
            z=l+r
        elif i=='-':
            z=l-r
        elif i=='*':
            z=l*r
        elif i=='**':
            z=l**r
        elif i=='/':
            z=l/r
        elif i=='//':
            z=l//r
        elif i=='%':
            z=l%r
        b.append(z)
print('Output:',b[0])