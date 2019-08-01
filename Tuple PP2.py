T1= ["A", "E","I","O","U"]
T2=[]
for i in T1:
    A= i*4
    T2.append(A)
print("The appended List", T2)

L1= ["12","22","33","Raj"," Richa", "12.99", "D"]
A= ""
for i in L1:
    A= A+i
print([A])

# For loop and Tuple problems
#.create a 4 element tuple that consists of a float, an integer, a Boolean value, and a string.  Assingn this tuple to a  variable.
# .print the tuple from step 1
# .print the the second element from the tuple you made in step 1
# .print the first element from the tuple you made in step 1
# .slice and print the first 3 elements of the tuple from step 1
# slice and print the last 3 elements of the tuple from step 1
# .slice and print the middle 2 elements of the tuple from step 1

T1= (12.2, 23,True," Raj")
print("The given Tuple is", T1)
print(T1[1])
print(T1[0])
print(T1[0:3])
print(T1[1:])
print(T1[1:3])

# For Loop Practice Problems:

# create a variable and assign it the tuple ("Bohr", "Leibniz", "Einstein")
# .create a variable and assign it an empty list
# create a variable and assign it the list [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# .use a for loop to go through and print each of the elements from the tuple in step 1 individually
# .use a for loop, flow control statement(s), and .append() to add the middle 6 elements to the empty list from step 2
# .print the new list


Var1= ("Bohr","Leibniz", "Einstein")
Var2= []
Var3= [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for element in Var1:
    print(element)
# Use a for loop, flow control statement(s), and .append() to add the middle 6 elements to the empty list from step 2
# print the new list

for i in Var3:
    if i>1 and i<8:
        Var2.append(i)
        print(i)
print("The newly created list is ", Var2)

