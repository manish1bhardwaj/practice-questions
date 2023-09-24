n=int(input())
a=0
b=1
while n>=b:
    
    if n%b==0:
       a+=1
    b+=1
if a==2:
  print('prime')
else:
    print('not prime')
 
