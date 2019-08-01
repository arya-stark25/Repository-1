# len() and str() practice
# create a variable and assign it the string "Python"
Var1= "Python"

# create another variable and assign it the length of the string assigned to the variable in step 1
Var2= len(Var1) # This function calculates the length of the String
print("The length of the String is=", Var2)


# create a variable and use string slicing and len() to assign it the length of the slice "yth" from the string assigned  to the variable from step 1
Var3=Var1[1:4]
print("The sliced string is =", Var3)
len1= len(Var3)
print("The length of the sliced String is=", len1)


# create a variable and assign it the float 1.32
float1= 1.32
Var5= str(float1) # This method converts the floating point number into String
print("This floating point number is converted into String =", Var5)
Var6= "1.32"[3:]
print("The new sliced String is=",Var6)


# create a variable and assign it the string "2" from the float assigned to the variable from the last problem (use the  str() string method for this)
Var7= "2"
len2= len(Var7) # This len() function calculates the length of the string
print("The length of the String is=",len2)


# create a variable and assign it the string "upper" changed to "UPPER" using .upper()
Var8= "upper"
StrUpp = Var8.upper()
print("This string has been converted into upper case letter =", StrUpp)


# create a variable and assign it the string "owe" from "LOWER" using string slicing and .lower()
Var9= "LOWER"
Strlow= Var9.lower()
Strlow= "lower"[1:4]
print("The sliced String is =", Strlow)

# Python reverse method
Str1= "Richa Pandey
Str2=Str1[-3:-1]
print(Str1)
print(Str1[:-3])
print(Str1[-3:])
print(Str1[-3:-1])
print(Str1[:9])
print(Str1[::2])
print(Str1[::-1])












