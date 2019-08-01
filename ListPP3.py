import math

# List Practice Problems Solutions:

# Create a 4 element list that consists of Values that are all Strings and assign it to a variable.
# Create a 3 element list that consists of values that are all numbers and assign it to a variable.
# Create a 5 element list that contains at least 1 String , 1 Number and 1 Boolean and assign it to a variable.
# print the list you created in step 1.
# Access by Index and print the second element of the list you made in step 2.
# Access by Index and print a boolean value from the list you made in step3.

L1= ["Raja", "Salim", "34","Maya"]
L2=[11,22,33]
L3=["Richa",45,True,78,"C"]
print(L1)
print(L2[1])
print(L3[2])

# Index Reassignment and .append():
# Create a variable and assign it the List [1,2,3]
# print the list from step 1
# reassign the first element in the list from Step 1 and value 2.
# reassign the second element in the list from Step 1 and value 3.
# reassign the third element in the list from Step 1 and value 4.
# use .append() to add the value 6 to the end of the list from the step1.
# .print the resulting list

L1=[1,2,3]
print(L1)
L1[0]=2
L1[1]=3
L1[2]=4
print(L1)
L1.append(6)
print("The New appended list is", L1)



# List Slicing

# create a 7 element list and assign it to a variable.
# slice the list from its first element to its fourth element and print the resulting 4 element list .
# slice the list from its third element to its fifth element and print the resulting 3 element list
# slice the list from its second element to its last element and print the resulting 6 element list.

L1= ["Raj", "Richa", True, False,"C",56,8]
print(L1[0:4])
print(L1[2:5])
print(L1[1:6])
print(L1[0:-1])
print(L1[-6:-1])
print(L1[-4:-2])

# .index() and .insert()


# .create a variable and assign it the list ["Bob Dylan", "Like a", "Rolling Stone"].
# .use the .index() function to find and print the index of the string "Rolling Stone" from the list in step 1.
# use the .insert() function to insert the string 1965 at index 0 of the list from step 1.
# print the list that results from step 3.


L1= ["Bob Dylan", "Like a", "Rolling Stone"]
print("The Index of element is", L1.index("Rolling Stone"))
L1.insert(0,1965)
print("The new list after insertion is",L1)


# .remove() and .pop().
# 1.create a variable and assign it the list ["McCartney", "Lennon", "Starr", "Harrison", "Sutcliffe"]
# .use .remove() to remove of the "Sutcliffe" from the list created in step 1.
# .print the new list
# .use .pop() to remove and print "Lennon" from the list
# .use .pop() to remove and print "Harrison" from the list
# .print the new list


L1=["McCartney", "Lennon", "Starr", "Harrison", "Sutcliffe"]
L1.remove("Sutcliffe")
print(L1)
L1.pop(1)
print(L1)
L1.pop() # L1.pop(2)
print(L1)

# print(dir(L1))
print(dir(math))




