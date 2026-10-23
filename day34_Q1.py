n=int(input('Enter the number:'))
c=0
a=n
while a>0:
    y=a&1
    a=a>>1
    if y==1:
        c=c+1
print(c)