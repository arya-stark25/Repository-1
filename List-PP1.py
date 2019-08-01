
mylist1= ["Ram", "K", "10", "12.33"]      # Creating List/ Defining List
print(mylist1[3])                     # Accessing List by Index Value
print(mylist1[0]+mylist1[1]+""+mylist1[2]+mylist1[3])     #doubt
A= ""
for i in mylist1:
    print(i)
    A=A+i
print("I am here",A)


print((mylist1[0]+mylist1[1]))
print("The concatenated List is", A)
print(print("--------------"))

# Can I do it too?
print("Hi")
print("The concatanated List is",(mylist1[0]+mylist1[1]))
print("Hello")
print(A)

# Re-assignment of elements in Python

#mylist1[2]= 5              # reassign the integer 5 at the index 2.
#print(mylist1)

# Inserting  an element into the list
# mylist1= ["Ram", "K", 10, 12.33]
mylist1.insert(2, "Raja Rabish Kumar")
print(mylist1)

# Inserting a value in List using append function

mylist1.append(89)
print(mylist1)

# Discover the length of the list

print("The length of the list is ", len(mylist1))

