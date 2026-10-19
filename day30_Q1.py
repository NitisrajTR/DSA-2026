def per(s):
    if len(s) == 1:
        return [s]
    a=[]
    for i in range(len(s)):
        z=s[i]
        y=s[:i]+s[i+1:]
        for j in per(y):
            a.append(z+j)
    return a
s=input('Enter the string: ')
for k in per(s):
    print(k)