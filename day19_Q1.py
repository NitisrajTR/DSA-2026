a=list(input('Brackets with no spaces: '))
b=[]
if a.count('(')!=a.count(')') or a.count('{')!=a.count('}') or a.count('[')!=a.count(']'):
    print('Not Balanced')
else:
    for i in range(len(a)):
        if a[i]=='(' or a[i]=='{' or a[i]=='[':
            b.append(a[i])
        elif a[i]==')':
            if len(b)>0 and b[-1]=='(':
                b.pop()
        elif a[i]=='}':
            if len(b)>0 and b[-1]=='{':
                b.pop()
        elif a[i]==']':
            if len(b)>0 and b[-1]=='[':
                b.pop()
    if len(b)==0:
        print('Balanced')
    else:
        print('Not Balanced')