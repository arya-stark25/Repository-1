# List declaration and basic methods practice


List1= [12,13.1, "Raj Kumar","K"]
print(List1[2])                     # accessing the elements in List using Index Operator
# print(List1[7])                     # Index Error: List Index is oou of range!!
A=(len(List1))                      # A= print(len(List1)----- ??
print("The length of the list is ",A)
List1.insert(6, "Cast away")        # Inserting elements/Items into the list
print(List1)
List1.append(89)                    # Appending Items into the List
print("The Appended List Is",List1)
List1.append(["Man In Black", "My Name is Khan", "Bande Matram"])
List1[3]= 56                        # Re-assigning the List Items
# List1[7]= 78                        # IndexError: list assignment index out of range
# print(List1)
#Newlist1= List1[0]+List1[3]         # Which operation is this??
#print(("The New List is",Newlist1)



# Index() Method: Searches the element in the List & Returns it's Index.
# However, if the same element is present more than once, index() method returns its smallest/first position

# Searching element in the Index & return the Index
print(List1)
I = List1.index("Cast away")
print("The Index of given Item is",I)

print("The Final String I have is", List1)

# Accessing the last element of the List in Python

RS=(List1[-1])
print("Reversed Indexing is", RS)

# remove method: Deleting the element from the List

List1.remove(89)                            # .remove function takes only 1 argument
print("List after removing the Item", List1)

# pop() function: To remove the element based on Index Number

List1.pop(3)
print("Popped List is", List1)

List1.pop()                              # pop(): blanked () removes only the last Item in the List
print(List1)

# Extending a List

#L1= ["a","b","c","d","e"]              # Can we pass single item in Extend Method? or Only the List
L1= [1,2,3,4,5]
L2= ["Ram","Shyam","P","S"]
(L1.extend(L2))
print(L1)
L1.extend("z")
print(L1)
L1.extend("k")
print(L1)
L1.extend("ö")
print(L1)
# L1.append(["Pro Sieben","I am only Legend"])
#L1.extend(12)   .# Why is this an Error?? "int" object is not iterable
#print(L1)
#L1.extend(13.1)     ## Why is this an Error?? "int" object is not iterable
print(L1)
print("The extended List is",L1)
print("my Lucky List", L1)

# List Indexing

SL1= [3,4,5,6,7,8,9,10,4,5,89]
sum= 0
for i in SL1:
    sum= i+ sum
print("The final Sum", sum)

print(SL1[2:7])
print(SL1[1:9])
print(SL1[0:11])
print(SL1[5:8])
print(SL1[7:10])
print(SL1[0:-2])
print(SL1[2:-3])
print(SL1[-6:-2])
print(SL1[-11:-8])



























