T1= ()
print("An Empty Tuple",T1)
T2= (12, 1.5, "Raja", True)
print("A hetrogeneous Tuple", T2)
T2= 34, "Raj", 12.34, False
print(" A Tuple without paranthesis", T2)
T4= 4, 4.4, "Python", ["C", 12.23]
print("A Tuple of mixed datataype", T4)
T5= (("X","y","z"),("x","y","z"))
print("A Tuple of Tuple", T5)
print("The length of Tuple is", len(T5))

print(T5[0])
print(T5[1])
# print(T5[2])  - Error: Tuple Index is out of range

# len()function to achieve he length of the tuple
V= ("a","e","i","o","u")
print(len(V))
print(V[1:4])
print(V[0:-1])
print(V[-4:-1])
print(V[-2:-1])
print(V[-2:-2])
print(V[1:5])
print(V[-1])     # Gives the last element
print(V[-2])

# Accessing the elements from the sub tuples

V= (("Jan","Feb","March"),("sun","Mon","Tue"),("Ram","Sita","Laxman"))
print(V[0][2])
print(V[1][2])
print(V[2][2])

V= (("Jan","Feb","March"),("sun","Mon","Tue"),[10,20,30,40])

# print(V[0][1]= "Dec")
# V[0][1]= "Dec"
# print(V)                # TypeError: 'tuple' object does not support item assignment
V[2][0]= 100
V[2][1]= 200
V[2][2]= 300
V[2][3]= 400
print(V)

V= ("Raj","Richa","Arya","R", 12, 12.33)
print("The new updated Tuple", V)

T= ("Sun","Mon","Tue","Wed")

NT= V+T
print("The Concatanated Tuple is", NT)

NT= NT*3
print(NT)

T1, T2 = ("R", "Raj", 5,12),("Sun","Mon","Tue")
print(T1+T2)

C= T.index("Mon")
print(C)
print(T.__dir__())

# Deleting elements in Tuple

T1= ("12", "23.33", "Shyam", "12.3rg","12", "23.33")
#del T1
#print( "Tuple after deleting the element", T1)
# This produces the following result. Note an exception raised, this is because after del tup tuple does not exist any more.
# NameError: name 'tup' is not defined

Red = T1.count("12")
print("Print the occurance of the element", Red)
T1.index("23.33")
print("print the Index of the given element",T1.index("23.33"))
# print(T1[::-1])
Z= reversed(T1)
print(tuple(z))








