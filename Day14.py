# 1. List down all the error types and check all the errors using a python program for all errors

#Name error
name="Bhuvanesh waran"
print(namee)

#type eror
a="123"
a+=123

Bhuvanesh=[1,2,3,4,5,6,7,8,9]
for i in range(2,Bhuvanesh):
    print(i+1)

#syntax error

for i range(1,10):
    print(i)

for="bhuvan"

#index error
Bhuvanesh = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(Bhuvanesh)):
    print(Bhuvanesh[i+1])

#module error
import Bhuvanesh

#key error
dict1=dict()
dict1={1:12,11:12,13:14}
print(dict1[14])

#import error
from math import Bhuvan

#value error
int("Bhuvanesh waran")

#Zero division error
a=100/0
print(a)


# 2. Design a simple calculator app with try and except for all use cases

def calculator():
    try:
        print("+")
        print("-")
        print("*")
        print("/")
        print("%")
        print("**")
        operation=input("enter the operator to perform: ")
        num1=int(input("enter number {0} ".format(1)))
        num2=int(input("enter number {0} ".format(2)))
        if operation == '+':
            print(num1 + num2)
        elif operation == '-':
            print(num1 - num2)
        elif operation == '*':
            print(num1 * num2)
        elif operation == '/':
            print(num1 / num2)
        elif operation == '%':
            print(num1 % num2)
        elif operation == '**':
            print(num1 ** num2)
        else:
            print('Invalid Input')
    except Exception as e:
        print(e)
calculator()

# 3. print one message if the try block raises a NameError and another for other errors

try:
    a=752
    if a==752:
        print(b)
        raise NameError("name error")
    if a > 0:
        raise ValueError("value error")
except NameError as e:
    print(e)
except ValueError as f:
    print(f)

# 4. When try-except scenario is not required?

         # Python Exceptions are error scenarios that alter the normal execution flow of the program The process of The code inside the else block is executed if there are no exceptions raised.

# 5. Try getting an input inside the try catch block
try:
    age=int(input("enter your age"))

except:
    print("ivalid value")