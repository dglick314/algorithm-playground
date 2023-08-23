### Calculator Project to study how python operations are done.
### This project is pretty simple and goes over the following operations
### User Input, Text scanning, loops and arithmetic.  
import re

#initialization
userInput = ""
output = ""
signCheck = ""
x=0
y=0

## Definitions
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
## Main
print("Hello, this is a calculator app. The following operations are supported.\n To add use +\n To subtract use -\nTo multiply use *\nTo divide use /\n\nThat concludes the available operations.\n")
userInput = input('Input the method + , - , * , /: ')
x = float(input('Enter the first value: '))
y = float(input('Enter the second value: '))

for signCheck in userInput: 
    if(signCheck == "+"):
        print("TEST : +!!")
        output = add(x,y)
    if(signCheck == "-"):
        print("TEST : -!!")
        output = subtract(x,y)
    if(signCheck == "*"):
        print("TEST : *!!")
        output = multiply(x,y)
    if(signCheck == "/"):
        print("TEST : /!!")
        output = divide(x,y)

print("Solution: ", output)
