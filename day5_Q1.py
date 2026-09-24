a=list(map(int,(input('Enter elements of list separated by space: ').split())))
k=int(input('Enter the value of k: '))
b=[]
for i in range(k):
    b=a[1:]+a[:1]
    a=b
print("The list after right rotation by", k, "positions is:", b)