a=list(map(int,(input('Enter numbers separated by space: ').split())))
b=0
for i in range(len(a)):
    b=b^a[i]
print(b)