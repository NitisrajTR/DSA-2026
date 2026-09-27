a=input('Enter a string: ')
a=a.strip()
c=a.lower()
c=c.replace(' ', '')
b=c[-1::-1]
if c==b:
    print(a,'is a Palindrome')
else:
    print(a,'is NOT a Palindrome')