#Write a program to loop through a list of numbers and add +2 to every value to elements in list

listbefore=[1,2,3,4,5,6,7,8,9]
k=2
listafter=[x + k for x in listbefore]
print("the {0} after {1}".format("list","addition"),listafter)


print()
print()

#Write a program to get the below pattern

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()


#Python Program to Print the Fibonacci sequence

n=int(input("enter the number of elements to print"))
n1,n2=0,1
count=2
if  n<= 0:
    print("enter valid number")
elif n==1 :
    print(n1)
else:
    print(n1)
    print(n2)
    while count < n:
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3
        count+=1

print()
print()

#•	Explain Armstrong number and write a code with a function

#A positive integer is called an Armstrong number of order n if abcd... = an + bn + cn + dn + ... In case of an Armstrong number of 3 digits, the sum of cubes of each digit is equal to the number itself. For example: 153 = 1*1*1 + 5*5*5 + 3*3*3 // 153 is an Armstrong number.

number=int(input("enter the number"))

temp=number
def amstrong(temp):
    sum = 0
    while temp> 0:
        r=temp%10
        sum=sum+(r*r*r)
        temp //=10
    if sum==number:
        print("{0} is amstrong number".format(number))
    else:
        print("{0} is not a amstrong number".format(number))

amstrong(temp)

print()
print()

#•	Write a program to print the multiplication table of 9

num=9
for i in range(1,11):
    print(num ,'x' ,i, '=',num*i)

print()
print()

#•	Check if a program is negative or positive

num = float(input("Enter a number: "))

if num > 0:
    print("{0} is a positive number".format(num))
elif num == 0:
    print("{0} is zero".format(num))
else:
    print("{0} is negative number".format(num))

print()
print()

#•	Write a program to convert the number of days to ages

days = int(input("enter number of days"))
year=int(days/365)
week= int((days%365) / 7)
day=abs((days - (year*365) + (week)))
print("years =",year)
print("weeks =",week)
print("days",day)

print()
print()

#•	Solve Trigonometry problem using math function write a program to solve using math function

import math
a=math.pi/6
print("value of sin pi/6 is : ",end="")
print(math.sin(a))
print("value of cos pi/6 is : ",end="")
print(math.cos(a))


print()
print()

#•	Create a calculator only on a code level by using if condition (Basic arithmetic calculation)

print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

# input choice
choice=int(input("Enter Choice(1-4): "))

if choice==1:
    a=int(input("Enter value 1:"))
    b=int(input("Enter value 2:"))
    c=a+b
    print("Sum = ",c)
elif choice==2:
    a = int(input("Enter value 1:"))
    b = int(input("Enter value 2:"))
    c=a-b
    print("Difference = ",c)
elif  choice==3:
    a = int(input("Enter value 1:"))
    b = int(input("Enter value 2:"))
    c=a*b
    print("Product = ",c)
elif choice==4:
    a = int(input("Enter value 1:"))
    b = int(input("Enter value 2:"))
    c=a/b
    print("Quotient = ",c)
else:
    print("Invalid Choice")
