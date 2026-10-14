a=list(map(int,(input('Enter numbers separated by space: ').split())))
k=int(input('Enter the value of k: '))
b=[]
z=len(a)-k+1
for i in range(z):
    c=a[i:i+k]
    d=sum(c)
    b.append(d)
print('Max sum:',max(b))