import time
n=int(input("enter the number"))
print('start')
while n:
    print(n)
    n-=1
    time.sleep(.5)
print('stop')    
