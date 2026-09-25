a=list(map(int,(input('Enter elements of the list separated by space: ').split())))
a.sort(reverse=True)
n=a[-1]
z=a[0]
b=[z]
if len(a)<3:
    print('Not enough elements(need at least 3)')
elif z==n:
    print('All elements are same,not enough unique elements,so 2nd and 3rd largest are same')
else:
    for i in a:
        if i!=b[-1]:
            b.append(i)
    if len(b)==2:
        print('Not enough unique elements,so 3rd largest is same as 2nd largest')
        print('2nd Largest:',b[1])
        print('3rd Largest:',b[1])
    else:
        print('2nd Largest:',b[1])
        print('3rd Largest:',b[2])