'''
Write a Python program to input basic salary of an employee and 
calculate its Gross salary according to following:
Basic Salary <= 10000 : HRA = 20%, DA = 80%
Basic Salary <= 20000 : HRA = 25%, DA = 90%
Basic Salary > 20000 : HRA = 30%, DA = 95%
'''
a=input()
b=float(input("enter the basic salary of employee"))

if  b<= 10000:
     HRA = b*0.2
     DA  = b*0.80
elif b <= 20000:
    HRA = b*0.25
    DA  = b*0.90
else :
    HRA = b*0.30
    DA  = b*0.95
gross = b+HRA+DA

print("name",a)
print("basic salary",b)
print("gross salary",gross)
