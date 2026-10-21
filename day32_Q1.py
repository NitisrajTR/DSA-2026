n=int(input('Enter the base number:'))
p=int(input('Enter power:'))
def power(a,b):
    if b==1:
        return(a)
    elif b==0:
        return(1)
    else:
        b=b-1
        c=a*power(a,b)
        return(c)
print(power(n,p))