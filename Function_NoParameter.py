# 1.define a function that takes no parameters and prints a string
# 2.create a variable and assign it the value 5
# 3.create a function that takes a single parameter and prints it
# 4.call the function you created in step 1
# 5.call the function you created in step 3 with the variable you made in step 2 as its input

def printstr():
    print("I am amazing")
var1=5
def printint(var1):
    print(var1)

printstr()
printint(5)


def magic(str, oper):
    if oper=="lower":
        return print(str.lower())


    elif oper=="upper":
        return print(str.upper())
    elif oper=="reverse":
        return print(str[::-1])
    else:
        return print(str)


magic("RaJKumaR","upper")
magic("RAJARam","lower")
magic("Sanam","reverse")




