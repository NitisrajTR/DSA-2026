"""
a=list(map(int,(input('Enter numbers separated by space: ').split())))
k=int(input('Enter the value of k: '))
b=[]
z=len(a)-k+1
for i in range(z):
    c=a[i:i+k]
    d=sum(c)
    b.append(d)
print('Max sum:',max(b))
"""

a=list(map(int,(input('Enter numbers separated by space: ').split())))
k=int(input('Enter the value of k: '))
b=[]
z=len(a)-k+1
d=sum(a[0:k])
for i in range(z):
    b.append(d)
    if i+k<len(a):
        d=d-a[i]+a[i+k]
print('Max sum:',max(b))