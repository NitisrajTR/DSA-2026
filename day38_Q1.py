a=int(input('Enter the number:'))
b=[500,200,100,50,20,10,5,2,1]
c=0
while a!=0:
    for i in b:
        if i<=a:
            z=a//i
            a=a%i
            c=c+z
            break
print(c)