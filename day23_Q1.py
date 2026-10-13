a=list(map(str, input('Enter words separated by space: ').split()))
d={}
for i in a:
    z="".join(sorted(i))
    if z not in d:
        d[z] = []
    d[z].append(i)
for i in d:
    print(*d[i])