n=int(input())
a=0
b=0
check=n
while n!=0:
    a=n%10
    b=b*10+a
    n=n//10
if check==b:
    print('palindrome')
else:
    print('not palindrome')
