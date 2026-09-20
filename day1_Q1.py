n=int(input('Enter no.of numbers:'))
a=[]
b=0
c=0
sum=0
for i in range(n):
    a.append(int(input(f'Enter number {i+1}: ')))
for j in a:
    sum=sum+j
    if j%2==0:
        b=b+1
    else:
        c=c+1
avg=sum/n
highest=max(a)
lowest=min(a)
print('Sum of the numbers is:', sum)
print('Average of the numbers is:', avg)
print('Highest number is:', highest)
print('Lowest number is:', lowest)
print('Number of even numbers is:', b)
print('Number of odd numbers is:', c)