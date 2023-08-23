### Calculator Project to study how python operations are done.
### This project is pretty simple and goes over the following operations
### User Input, Text scanning, loops and arithmetic.  



userInput = ""
x = ""
print("Hello, this is a calculator app. The following operations are supported.\n To add use +\n To subtract use -\nTo multiply use *\nTo divide use /\n\nThat concludes the available operations.\n")
userInput = input('Input the problem: ')
for x in userInput: 
    if(x == "+"):
        print("TEST : +!!")

    if(x == "-"):
        print("TEST : -!!")

    if(x == "*"):
        print("TEST : *!!")

    if(x == "/"):
        print("TEST : /!!")
