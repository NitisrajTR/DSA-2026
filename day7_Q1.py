s=input("Enter a string: ")
a=0
b=[' ']
for i in s:
    if i not in b:
        b.append(i)
        for j in s:
            if i==j:
                a+=1
        print(f"{i}: {a}")
    a=0