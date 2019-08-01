"""
How to access the characters in the string using Index
How to slice the string

"""

# Accessing the characters from the String
Str= "Richa"
p1= Str[0]
p2=Str[1]
# This is how we access the character directly from the String
p3="Richa"[4]
p4= Str[-1]  # In Python index position -1 indicates the last item of a sequence.
p5=Str[-2]
p6=Str[-3]
print(" Accessed characters from the String")
print(p1,p2,p3,p4,p5,p6)

# Slicing the string

Mystr= "HelloWorld"

s1= Mystr[:4]
s2= Mystr[3:5] # Here 3 represent the index [3]=l
s3= Mystr[5:]
print("Here is the output of the sliced string")
print(s1,s2,s3)

