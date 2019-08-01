
 import sys

choice= int(input("Enter the option 1,2 or 3"))


if choice==1:
    price=1.00
    print("Fetch the Water Bottle")


elif choice== 2:
    price = 1.5
    print("Fetch the Cola Bottle")


elif choice==3:
    price = 2.00
    print("Fetch the gatorade Bottle")

else:
    sys.exit("Wrong Choice")

Q= int(input("Enter the number of Quarter"))
D= int(input("Enter the number of dimes"))
N= int(input("Enter the number of Nickel"))
P=int(input("Enter the number of Penny"))

Sum= Q*0.25+D*0.1+N*0.05+P*0.01

