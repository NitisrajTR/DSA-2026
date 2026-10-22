a=input('Enter the string:')
def rev(z):
    b=list(z)
    if len(b)>1:
        y=rev(b[1:])+b[0]
        return(y)
    else:
        return(b[0])
print(rev(a))