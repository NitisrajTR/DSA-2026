n=int(input('Enter the number:'))
k=int(input('Enter the bit position:'))
a=n>>k
a=a&1
print(a)