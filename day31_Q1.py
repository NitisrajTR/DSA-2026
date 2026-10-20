n=int(input('Enter the number:'))
def sum(z):
    t=z%10
    r=z//10
    if r>9:
        r=sum(r)
        return(t+r)
    else:
        return(t+r)
a=sum(n)
print('sum of numbers:',a)