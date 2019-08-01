# Here ,I am practicing the python escape sequences
# Strings and Escape Sequences review
# 1. print a string surrounded by single quotes
# 2. print a string surrounded by double quotes
# 3. Use an escape sequence to surround the "in quotes" from the String "This should be in quotes". in double quotes.
# 4. create the variable and assign it the string "Alligator".
# 5. access the "a" from the variable you crated in the step4 by index and print it.
# 6. print the slice "Alli" from the variable created in the step 4.
# 7. print the slice "gat" from the variable created in step 4.
# 8. print the slice "tor" from the variable created in step 4.

print("Enter the String Values")
Str1= 'Rajkumar'
Str2= "Richapandey"
print("This should be \"in quotes \".")
Str3= "Alligator"
# Var1= Str3[5]
Var2= "Alligator"[5]
print(Var2)
# print("Access the variable at the Index 5 =", Var1)
Var3= Str3[:4]  # It access the index values at [0],[1],[2],[3].
Var4= Str3[4:7] #
Var5= Str3[6:]  #
print("Print the sliced string parts respectively")
# print("Var1=",Var1)
print("Var3=\n",Var3)
print("Var4=\n", Var4)
print("Var5=\n", Var5)
print("This program ends here\n")

# Here begines the part-2 of this program.

# 1.create a variable and assign a string that is surrounded in double quotes to it
# 2.create a variable and assign a string that is surrounded in single quotes to it
# 3.create a variable and assign it a string that uses the double quote escape sequence within it
# 4.create a variable and assign it a string that uses the single quote escape sequence within it



V1= "Suzi"
V2= 'Lusi'
V3= print("I am \"gonna wish \ her")
print(V3)

# Here begins the part 3 of the program
# accessing values by index and string slicing
# 1.create a variable called lannisters and assign it the string "JaimeCerseiTyrion"
# 2.create a variable and assign it the "a" from the string assigned to the variable lannisters.
# 3.create a variable and assign it the "J" from the string assigned to the variable lannisters.
# 4.create a variable and assign it "Jaime" from the string assigned to the variable lannisters.
# 5.create a variable and assign it "Cersei" from the string  assigned to the variable lannisters.
# 6.create a variable and assign it "Tyrion" from the string assigned to the variable Lannisters.


lannisters= "JaimeCerseiTyrion"
V1="JaimeCerseiTyrion"[1]  #a" from the string assigned to the variable lannisters.
V2="JaimeCerseiTyrion"[0]  #"J" from the string assigned to the variable lannisters.
V3="JaimeCerseiTyrion"[:5] #"Jaime" from the string assigned to the variable lannisters.
V4="JaimeCerseiTyrion"[5:11] #"Cersei" from the string  assigned to the variable lannisters.
V5="JaimeCerseiTyrion"[11:] #"Tyrion" from the string assigned to the variable Lannisters.

print("Here the system prints the variables")
print("V1=", V1)
print("V2=", V2)
print("V3=", V3)
print("V4=", V4)
print("V5=", V5)
print("This program ends here")









