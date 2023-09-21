import time
p= 'manish'
b=3
while True:
    a=input('enter password:')
    if p==a:
       print('correct password')
       break
    else:
        print('incorrect password')
        time.sleep(0.5)
        
    
    
